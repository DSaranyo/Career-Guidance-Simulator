
def suggest_colleges(rank, stream):
    colleges = []

    if stream == "Science":
        if rank <= 10000:
            colleges = ["IIT Bombay", "IIT Delhi", "IIT Madras"]
        elif rank <= 30000:
            colleges = ["NIT Trichy", "NIT Surathkal", "IIIT Hyderabad"]
        elif rank <= 70000:
            colleges = ["IIIT Bhubaneswar", "DTU", "NSUT"]
        else:
            colleges = ["Local Government Colleges", "Private Engineering Colleges"]

    elif stream == "Commerce":
        colleges = ["Shri Ram College of Commerce", "St. Xavier’s Kolkata", "Christ University", "Loyola College"]

    elif stream == "Arts":
        colleges = ["Lady Shri Ram College", "JNU Delhi", "Presidency University", "Delhi University Colleges"]
    
    return colleges


def suggest_careers(stream):
    if stream == "Science":
        return {
            "Data Science": [
                "Learn Python & Statistics",
                "Do projects using real-world data",
                "Earn a BTech/BE in CS or IT",
                "Pursue internships and certifications (e.g. Kaggle, Coursera)"
            ],
            "Cybersecurity": [
                "Learn Networking & Linux basics",
                "Get certified (CEH, CompTIA Security+)",
                "Pursue BTech in Cybersecurity or CS",
                "Do ethical hacking projects and bug bounties"
            ],
            "AI/ML": [
                "Study Math (Linear Algebra, Probability)",
                "Learn Python & ML frameworks",
                "Earn CS/AI degree",
                "Do research or industry projects"
            ],
            "Medical": [
                "Appear for NEET",
                "Get MBBS degree",
                "Do specialization (e.g., cardiology)",
                "Open clinic or work at hospitals"
            ]
        }

    elif stream == "Commerce":
        return {
            "Chartered Accountant": [
                "Register for CA Foundation after 12th",
                "Pass all 3 levels (Foundation, Intermediate, Final)",
                "Do articleship",
                "Get CA license"
            ],
            "Investment Banker": [
                "Earn B.Com or BBA",
                "Get MBA in Finance",
                "Intern in finance companies",
                "Join banks or firms"
            ],
            "Entrepreneur": [
                "Learn business skills",
                "Start small business in college",
                "Join incubators",
                "Pitch to investors"
            ]
        }

    elif stream == "Arts":
        return {
            "Psychologist": [
                "Get BA in Psychology",
                "Do MA/MSc in Psychology",
                "Earn certifications (Counseling, Clinical)",
                "Start practice or join hospital"
            ],
            "Journalist": [
                "Pursue BA in Journalism/Mass Comm",
                "Intern with media houses",
                "Build a portfolio (blog, YouTube)",
                "Join media organizations"
            ],
            "Civil Services": [
                "Graduate from any stream",
                "Prepare for UPSC exams",
                "Clear Prelims, Mains, Interview",
                "Join IAS/IPS/IFS"
            ]
        }

    return {}


# Main program
print("=== Career Guidance System ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
stream = input("Enter your stream (Science, Commerce, Arts): ").strip().capitalize()

jee_rank = 0
if stream == "Science":
    jee_rank = int(input("Enter your JEE Main rank: "))

print("\nHello", name + "!")
print("You are", age, "years old and have chosen the", stream, "stream.\n")

# College Suggestions
print("🏫 Suggested Colleges:")
colleges = suggest_colleges(jee_rank, stream)
for col in colleges:
    print("- " + col)

# Career Suggestions
print("\n💼 Career Options & Roadmap:")
careers = suggest_careers(stream)
for career, steps in careers.items():
    print("\n👉 " + career + " Career Plan:")
    for i, step in enumerate(steps, start=1):
        print(f"   Step {i}: {step}")

print("\n🔚 Thank you for using the Career Guidance System!")
