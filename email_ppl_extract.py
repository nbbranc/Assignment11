'''
    Walker Yturbides
    CS5001, Fall 2025
    Practice Exam

    Exam Review - Practice Problems.
    Email Parser
'''
def parse_institution(domain: str) -> str:
    """Convert short domain prefixes into readable institution names."""
    domain_map = {
        'bu': 'Boston University',
        'mit': 'MIT',
        'harvard': 'Harvard University',
        'yale': 'Yale University',
        'company': 'Company',
        'org': 'Organization',
        'edu': 'Educational Institution',
    }

    # Take the first section before the top-level domain (e.g., bu.edu → bu)
    parts = domain.split('.')
    '''
    NB Comment 1: 
    domain_parts[0] is not lowercased before the domain_map lookup, 
    so uppercase domains like BU.EDU silently fall back to key.capitalize() 
    instead of matching the correct institution.
    '''
    if len(parts) >= 1:
        key = parts[0]
        return domain_map.get(key, key.capitalize())
    return domain.capitalize()


def extract_emails_and_people(text: str) -> tuple:
    """
    Returns two lists:
    1. all_emails -> all emails found in the text
    2. people -> structured info for emails of the form last.first@domain.institution
    """
    all_emails = []
    people = []

    words = text.replace('\n', ' ').split(' ')

    for word in words:
        word = word.strip('.,!?;:()[]{}"\'<>')

        if '@' in word and '.' in word:
            parts = word.split('@')
            if len(parts) == 2:
                username, domain = parts

                # Add to all emails list
                '''
                NB Improvement:
                all_emails should only append after all validation 
                passes, so it only contains properly validated emails.
                Maybe it emails should be added to the list towards 
                the end when it has been validated
                '''
                all_emails.append(word)

                # Check if username matches last.first pattern
                username_parts = username.split('.')
                domain_parts = domain.split('.')
                '''
                NB Comment 2:
                No minimum or maximum length checking is enforced on the 
                username parts. Very short or superlong strings would 
                pass, since those bounds aren't checked
                '''

                if len(username_parts) == 2 and username_parts[0].isalpha() and username_parts[1].isalpha():
                    '''
                    NB Comment 3: 
                    isalpha() rejects valid email characters like underscores
                    and hyphens, causing valid emails to be silently 
                    excluded from people.
                    '''
                    last, first = username_parts
                    institution = parse_institution(domain_parts[0])
                    name = f"{first.capitalize()} {last.capitalize()}"
                    people.append({
                        'name': name,
                        'institution': institution
                    })

    return all_emails, people

def main():
    text = (
    "Hello- World1,Contact doe.jane@Bu.Edu, Today_ is my birthday "
    "smith.john@mit.edu, brown.sara@company.org, loving it! "
    "support@gmail.com, admin@my-site.net, user123@yahoo.com"
    )
    emails, people = extract_emails_and_people(text)
    
    print("All emails:", emails)
    print("People info:", people)   


if __name__ == "__main__":
    main()