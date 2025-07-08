from bs4 import BeautifulSoup

# Load the HTML content from the file
with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extract all testimonial articles
testimonials = soup.select("section:has(h2:contains('Testimonials')) article")

# Expected data
expected_texts = [
    "I am completely blown away. Thanks to Techium, we've just "
    "launched our 5th website!",
    "Thank you so much for your help. Techium company is awesome!",
    "I love your system. Definitely worth the investment. I'd be "
    "lost without Techium company."
]

expected_authors = ["Yuri Y.", "Dorrie S.", "Sven H."]

# Check and print results
for i in range(3):
    quote = testimonials[i].blockquote
    cite = quote.cite

    text_correct = expected_texts[i] in quote.text.strip()
    author_correct = cite and cite.text.strip() == expected_authors[i]

    ordinal = ['first', 'second', 'third'][i]
    print(f"{ordinal} article has correct text: {text_correct}")
    print(f"{ordinal} author cited correctly: {author_correct}")
