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
                all_emails.append(word)

                # Check if username matches last.first pattern
                username_parts = username.split('.')
                domain_parts = domain.split('.')
                if len(username_parts) == 2 and username_parts[0].isalpha() and username_parts[1].isalpha():
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
    "Hello- World1,Contact doe.jane@bu.edu, Today_ is my birthday smith.john@mit.edu, brown.sara@company.org, loving it! "
    "support@gmail.com, admin@my-site.net, user123@yahoo.com"
    )
    emails, people = extract_emails_and_people(text)
    
    print("All emails:", emails)
    print("People info:", people)   


if __name__ == "__main__":
    main()