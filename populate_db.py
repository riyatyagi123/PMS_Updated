import sqlite3
import json
from datetime import datetime, timedelta

def populate():
    db_path = "database.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Clear existing data from operational tables
    tables_to_clear = ["goals", "feedback", "probation_reviews", "review_cycles", "feedback_responses", "email_logs"]
    for t in tables_to_clear:
        cur.execute(f"DELETE FROM {t}")
    
    # Recreate users to ensure exact IDs for referencing
    cur.execute("DELETE FROM users")
    
    users = [
        # id=1: Amit Patel
        (1, 'Amit Patel', 'amit@example.com', '123', 'employee', '2026-02-25', 'bi-annual'),
        # id=2: Riya Sharma
        (2, 'Riya Sharma', 'riya@example.com', '123', 'employee', '2026-03-01', 'bi-annual'),
        # id=3: Dipali Sen
        (3, 'Dipali Sen', 'dipali@example.com', '123', 'employee', '2026-04-01', 'bi-annual'),
        # id=4: Vikram Malhotra (Manager 1)
        (4, 'Vikram Malhotra', 'mgr@gmail.com', '123', 'manager', '2026-01-01', 'bi-annual'),
        # id=5: Sanjay Gupta (Manager 2)
        (5, 'Sanjay Gupta', 'mgr2@example.com', '123', 'manager', '2026-01-15', 'bi-annual'),
        # id=6: Arjun Mehta (Admin 1)
        (6, 'Arjun Mehta', 'admin@gmail.com', '123', 'admin', '2026-01-01', 'bi-annual'),
        
        # Additional Indian employees/managers to enrich the platform
        # id=7: Neha Reddy
        (7, 'Neha Reddy', 'neha@example.com', '123', 'employee', '2026-03-10', 'quarterly'),
        # id=8: Rohan Verma
        (8, 'Rohan Verma', 'rohan@example.com', '123', 'employee', '2026-04-05', 'bi-annual'),
        # id=9: Ananya Iyer
        (9, 'Ananya Iyer', 'ananya@example.com', '123', 'employee', '2026-02-10', 'quarterly'),
        # id=10: Rajesh Kumar
        (10, 'Rajesh Kumar', 'rajesh@example.com', '123', 'manager', '2026-01-10', 'bi-annual'),
        # id=11: Priya Rao
        (11, 'Priya Rao', 'priya@example.com', '123', 'manager', '2026-01-20', 'bi-annual'),
        # id=12: Karan Johar
        (12, 'Karan Johar', 'karan@example.com', '123', 'admin', '2026-01-01', 'bi-annual'),
        # id=13: Aditya Roy
        (13, 'Aditya Roy', 'aditya@example.com', '123', 'admin', '2026-01-01', 'bi-annual')
    ]
    
    cur.executemany("INSERT INTO users (id, name, email, password, role, doj, review_track) VALUES (?, ?, ?, ?, ?, ?, ?)", users)
    print("Users seeded successfully.")

    # 1. GOALS
    # Goal 1 (submitted 8 days ago -> triggers 1 Goal Approval escalation)
    goals = [
        # Pending Approval
        (1, 'G-001', 'Revamp Enterprise Dashboard UI', 'Redesign the main analytics widgets and sidebar navigation for glassmorphic style.', 1, 'Pending Approval', 30, 0, (datetime.now() - timedelta(days=8)).isoformat(), None, 'individual'),
        (2, 'G-002', 'Optimize Database Queries', 'Add indexes and rewrite complex joins to reduce dashboard page load time to < 200ms.', 2, 'Pending Approval', 25, 0, datetime.now().isoformat(), None, 'individual'),
        (3, 'G-003', 'Implement OAuth2 Authentication', 'Integrate Google and Microsoft single sign-on options for enterprise tenants.', 3, 'Pending Approval', 20, 0, datetime.now().isoformat(), None, 'individual'),
        (4, 'G-004', 'Automate PDF Report Generation', 'Set up a weekly scheduler that exports goal completion metrics to PDF and emails HR.', 7, 'Pending Approval', 15, 0, datetime.now().isoformat(), None, 'individual'),
        (5, 'G-005', 'Setup CI/CD Pipeline', 'Configure GitHub Actions to run unit tests and build docker images on every push.', 8, 'Pending Approval', 10, 0, datetime.now().isoformat(), None, 'individual'),
        
        # Active
        (6, 'G-006', 'Refactor Email Service Logic', 'Migrate from local SMTP to Sendgrid API to improve notification delivery rates.', 1, 'Active', 20, 45, (datetime.now() - timedelta(days=15)).isoformat(), None, 'individual'),
        (7, 'G-007', 'Conduct User Security Training', 'Ensure all team members complete the annual security compliance modules.', 2, 'Active', 10, 80, (datetime.now() - timedelta(days=10)).isoformat(), None, 'individual'),
        (8, 'G-008', 'Develop Sentiment Analysis Engine', 'Write a mini python utility using textblob to score feedback responses automatically.', 3, 'Active', 30, 60, (datetime.now() - timedelta(days=20)).isoformat(), None, 'individual'),
        (9, 'G-009', 'API Rate Limiting & Security', 'Apply flask-limiter to protect auth endpoints and public APIs from brute force attacks.', 7, 'Active', 25, 20, (datetime.now() - timedelta(days=12)).isoformat(), None, 'individual'),
        (10, 'G-010', 'Write Comprehensive Integration Tests', 'Increase test coverage for review cycle triggers and probation reviews by 15%.', 9, 'Active', 15, 30, (datetime.now() - timedelta(days=14)).isoformat(), None, 'individual'),
        
        # Completed
        (11, 'G-011', 'Setup Database Backups', 'Configure daily automated database snapshots uploaded to AWS S3 buckets.', 1, 'Completed', 10, 100, (datetime.now() - timedelta(days=30)).isoformat(), None, 'individual'),
        (12, 'G-012', 'Initial Launch of PMS Platform', 'Successfully deploy the beta version of the Goal Management System.', 2, 'Completed', 30, 100, (datetime.now() - timedelta(days=25)).isoformat(), None, 'individual'),
        (13, 'G-013', 'Design System Blueprint', 'Document component styles, colors, and layout guidelines in Figma.', 3, 'Completed', 20, 100, (datetime.now() - timedelta(days=22)).isoformat(), None, 'individual'),
        (14, 'G-014', 'Fix High Priority Memory Leaks', 'Profile memory usage under load and resolve leak in background thread execution.', 7, 'Completed', 25, 100, (datetime.now() - timedelta(days=18)).isoformat(), None, 'individual'),
        (15, 'G-015', 'Prepare Q1 Goal Summary', 'Compile goal completion rates across departments and present to executives.', 8, 'Completed', 15, 100, (datetime.now() - timedelta(days=16)).isoformat(), None, 'individual')
    ]
    cur.executemany("INSERT INTO goals VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", goals)
    print("Goals seeded successfully.")

    # Goal Feedback
    goal_feedbacks = [
        (1, 1, 4, 11, 5, 'Exceptional deployment stability! Backups work flawlessly.'),
        (2, 2, 4, 12, 4, 'Great work launching the platform, minor visual bug fixed quickly.'),
        (3, 3, 5, 13, 3, 'Design system guidelines are solid, but could use more component detail.'),
        (4, 7, 10, 14, 5, 'Outstanding work fixing complex memory leaks. Clean architecture.'),
        (5, 8, 10, 15, 4, 'Good summary prepared, met the requested deadlines.')
    ]
    cur.executemany("INSERT INTO feedback VALUES (?, ?, ?, ?, ?, ?)", goal_feedbacks)
    print("Goal Feedbacks seeded successfully.")

    # 2. PROBATION REVIEWS
    # Review 4 (Dipali, doj=2026-04-01 is old, stage=30 review is overdue pending manager -> triggers 1 probation escalation)
    probation_reviews = [
        # 1. Amit Patel (id 1): Day 30 - Completed
        (1, 1, 30, 
         json.dumps({"comfort": "Very comfortable with the tech stack", "clarity": "Highly clear requirements", "challenges": "No major blockers"}),
         json.dumps({"understanding": "Demonstrates fast learning", "performance": "Exceeds goals set so far", "concerns": "None"}),
         1, 1, '2026-03-27'),
         
        # 2. Riya Sharma (id 2): Day 30 - Completed
        (2, 2, 30, 
         json.dumps({"comfort": "Great culture fit, learning quickly", "clarity": "Good direction from manager", "challenges": "Getting up to speed with database schemas"}),
         json.dumps({"understanding": "Active contributor", "performance": "Excellent progress on UI redesign", "concerns": "Keep working on SQL performance"}),
         1, 1, '2026-04-10'),
         
        # 3. Amit Patel (id 1): Day 60 - Completed
        (3, 1, 60, 
         json.dumps({"comfort": "Fully integrated into team and leading small initiatives", "clarity": "Complete alignment with technical roadmap", "challenges": "None"}),
         json.dumps({"understanding": "Superb understanding of core system architecture", "performance": "Solid delivery on key goals", "concerns": "None"}),
         1, 1, '2026-05-08'),

        # 4. Dipali Sen (id 3): Day 30 - Overdue Pending Manager Submission (triggers 1 probation escalation!)
        (4, 3, 30,
         json.dumps({"comfort": "Good onboarding experience, helpful peers", "clarity": "Tasks are well defined", "challenges": "Integrating APIs took slightly longer than planned"}),
         None,
         1, 0, '2026-05-12'),

        # 5. Neha Reddy (id 7): Day 30 - Completed
        (5, 7, 30,
         json.dumps({"comfort": "Adjusted well to the team and project structure", "clarity": "Tasks are clear", "challenges": "Setting up the custom build environment"}),
         json.dumps({"understanding": "Deep understanding of codebase logic", "performance": "Excellent initial delivery", "concerns": "None"}),
         1, 1, '2026-04-15'),
          
        # 6. Rohan Verma (id 8): Day 30 - Completed
        (6, 8, 30,
         json.dumps({"comfort": "Onboarding was highly organized, feel very welcomed", "clarity": "Good alignment on milestones", "challenges": "Understanding complex data-flow diagrams"}),
         json.dumps({"understanding": "Shows strong technical promise", "performance": "Making steady progress", "concerns": "None"}),
         1, 1, '2026-05-18')
    ]
    cur.executemany("INSERT INTO probation_reviews VALUES (?, ?, ?, ?, ?, ?, ?, ?)", probation_reviews)
    print("Probation reviews seeded successfully.")

    # 3. REVIEW CYCLES
    review_cycles = [
        # Amit Patel (Cycle 2 2025)
        (1, 1, 'bi-annual', 'Cycle 2 (2025)', '2025-10-01', '2026-03-31', 1, 1,
         json.dumps({"rating": "Above Expectations", "achievements": "Launched the core platform services ahead of time.", "challenges": "Had issues with legacy SMTP config."}),
         json.dumps({"rating": "Above Expectations", "comment": "Excellent technical competence and high ownership."}),
         '2026-03-25'),
          
        # Riya Sharma (Cycle 2 2025)
        (2, 2, 'bi-annual', 'Cycle 2 (2025)', '2025-10-01', '2026-03-31', 1, 1,
         json.dumps({"rating": "Meets Expectations", "achievements": "Contributed to dashboard mockup design and code integrations.", "challenges": "Tuning database query speeds."}),
         json.dumps({"rating": "Meets Expectations", "comment": "Solid designer and team player. Keep expanding back-end skills."}),
         '2026-03-26'),

        # Neha Reddy (Q1 2026)
        (3, 7, 'quarterly', 'Q1 (2026)', '2026-01-01', '2026-03-31', 1, 1,
         json.dumps({"rating": "Above Expectations", "achievements": "Delivered the PDF exporter service module.", "challenges": "Aligning on styling guidelines."}),
         json.dumps({"rating": "Above Expectations", "comment": "Excellent developer, works quickly and efficiently."}),
         '2026-04-02'),

        # Amit Patel (Cycle 1 2026)
        (4, 1, 'bi-annual', 'Cycle 1 (2026)', '2026-04-01', '2026-09-30', 1, 1,
         json.dumps({"rating": "Above Expectations", "achievements": "Currently migrating email service and scaling system pipeline.", "challenges": "Resource constraints in team."}),
         json.dumps({"rating": "Above Expectations", "comment": "Outstanding technical skills and excellent team coordination. Delivered on all targets."}),
         '2026-06-02'),

        # Dipali Sen (Cycle 1 2026)
        (5, 3, 'bi-annual', 'Cycle 1 (2026)', '2026-04-01', '2026-09-30', 1, 1,
         json.dumps({"rating": "Meets Expectations", "achievements": "Contributed to design system blueprints and user settings module.", "challenges": "Learning custom styling utilities."}),
         json.dumps({"rating": "Meets Expectations", "comment": "Good progress on design modules. Solid teamwork and high receptivity to feedback."}),
         '2026-06-03')
    ]
    cur.executemany("INSERT INTO review_cycles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", review_cycles)
    print("Review Cycles seeded successfully.")

    # 4. FEEDBACK RESPONSES
    feedback_responses = [
        # Older flags are marked as 'resolved'
        (1, 1, 'employee', 'goal', 6,
         json.dumps({"comment": "This task is causing a lot of stress. I have major issues with local database memory limitations and the timeline is too tight."}),
         2, 'negative', 1, 'Negative Sentiment, Low Rating', 'resolved', 'Provided memory profiling guides and allocated dedicated sandbox resources.',
         (datetime.now() - timedelta(days=10)).isoformat(), 6),
         
        (2, 2, 'employee', 'probation', 2,
         json.dumps({"comment": "I am feeling extremely poor onboarding assistance. The setup instructions do not work, and I have a major problem setting up Docker."}),
         1, 'negative', 1, 'Negative Sentiment, Low Rating', 'resolved', 'Conducted one-on-one session to walk through Docker configurations.',
         (datetime.now() - timedelta(days=8)).isoformat(), None),

        # Recent flags (under 7 days -> age 2 days, so not escalated)
        (3, 3, 'employee', 'cycle', 5,
         json.dumps({"achievements": "", "challenges": "I had a bad experience trying to complete the database scaling goal alone."}),
         2, 'negative', 1, 'Negative Sentiment, Incomplete Response', 'pending', None,
         (datetime.now() - timedelta(days=2)).isoformat(), None),

        # Resolved
        (4, 7, 'employee', 'goal', 9,
         json.dumps({"comment": "This rate limiting library is very poor and has a memory leak issue."}),
         2, 'negative', 1, 'Negative Sentiment, Low Rating', 'resolved', 'Assigned Sanjay to support Neha with library configurations.',
         (datetime.now() - timedelta(days=12)).isoformat(), 9),
         
        (5, 9, 'employee', 'goal', 10,
         json.dumps({"comment": "Very bad documentation. A huge problem trying to get unit tests working."}),
         1, 'negative', 1, 'Negative Sentiment, Low Rating', 'resolved', 'Updated documentation and added boilerplates.',
         (datetime.now() - timedelta(days=15)).isoformat(), 10),
         
        # Recent flag (under 7 days -> age 1 day, so not escalated)
        (6, 1, 'employee', 'goal', 11,
         json.dumps({"comment": "Our backup server is poor and we had a database connection issue today."}),
         2, 'negative', 1, 'Negative Sentiment, Low Rating', 'pending', None,
         (datetime.now() - timedelta(days=1)).isoformat(), 11)
    ]
    cur.executemany("INSERT INTO feedback_responses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", feedback_responses)
    print("Feedback Responses seeded successfully.")

    # 5. EMAIL LOGS
    email_logs = [
        (1, 1, 'amit@example.com', 'probation', 'Probation Review (30 Days) is due', 'sent', (datetime.now() - timedelta(days=73)).isoformat()),
        (2, 4, 'mgr@gmail.com', 'probation', 'Manager Action Required: Probation Review for Amit Patel (30 Days)', 'sent', (datetime.now() - timedelta(days=73)).isoformat()),
        (3, 1, 'amit@example.com', 'reminder', 'REMINDER: Probation Review (30 Days) pending', 'sent', (datetime.now() - timedelta(days=71)).isoformat()),
        (4, 2, 'riya@example.com', 'probation', 'Probation Review (30 Days) is due', 'sent', (datetime.now() - timedelta(days=59)).isoformat()),
        (5, 4, 'mgr@gmail.com', 'probation', 'Manager Action Required: Probation Review for Riya Sharma (30 Days)', 'sent', (datetime.now() - timedelta(days=59)).isoformat()),
        
        # Recent notifications
        (6, 6, 'admin@gmail.com', 'probation', 'Day 30 Probation Review successfully completed for Dipali Sen', 'sent', (datetime.now() - timedelta(hours=2)).isoformat()),
        (7, 6, 'admin@gmail.com', 'goal', 'New goal G-001 submitted for approval by Amit Patel', 'sent', (datetime.now() - timedelta(hours=4)).isoformat()),
        (8, 6, 'admin@gmail.com', 'feedback', 'Resolved negative feedback response flag for Riya Sharma', 'sent', (datetime.now() - timedelta(hours=5)).isoformat())
    ]
    cur.executemany("INSERT INTO email_logs VALUES (?, ?, ?, ?, ?, ?, ?)", email_logs)
    print("Email logs seeded successfully.")

    conn.commit()
    conn.close()
    print("ALL SEEDING COMPLETED successfully.")

if __name__ == '__main__':
    populate()
