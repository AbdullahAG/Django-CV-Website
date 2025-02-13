from django.shortcuts import render

def home(request):
    context = {
        'name': 'Abdullah Alghofaili',
        'email': 'aaalghofaili@gmail.com',
        'phone': '+1 (619) 913 - 6357',
        'github': 'AbdullahAG',
        'linkedin': 'aaalghofaili',
        'skills': {
            'languages': ['Java', 'Python', 'Golang', 'C/C++'],
            'tools': ['Splunk', 'Wireshark', 'Burp Suite', 'Snort', 'Nessus', 'Nmap', 'Metasploit', 'Aircrack-ng', 'Autopsy', 'FTK', 'Ghidra']
        },
'experience': [
            {
                'title': 'Lecturer',
                'organization': 'King Saud University',
                'dates': 'May 2020 - Present',
                'tasks': [
                    'Manage the lab section for courses like Information Security, Computer Network, Database Management Systems, Mathematical Modeling.',
                    'Design, administer, and assess student exams and assignments.',
                    'Illustrate tools like Metasploitable, Wireshark, MySQL, Java.'
                ]
            },
            {
                'title': 'Facilitator',
                'organization': 'SANS Institute',
                'dates': 'Aug 2021',
                'tasks': [
                    'Facilitated and mentored for SEC560: Network Penetration Testing and Ethical Hacking at SANS Virginia Beach 2021 Event.'
                ]
            },
            {
                'title': 'Security Fellow',
                'organization': 'Insight Data Science',
                'dates': 'May 2020 - Aug 2020',
                'tasks': [
                    'Developed a Python tool called “PPP-PythonPythonPython” that works on Python scripts to report a highly scrambled obfuscated code through data confusion, naming obfuscation, and dead code insertion.'
                ]
            },
            {
                'title': 'Teaching Assistant',
                'organization': 'Johns Hopkins University',
                'dates': 'Jan 2020 - May 2020',
                'tasks': [
                    'Implemented and created Seed labs that dealt with Firewalls and Intrusion Detection. Assisted with illustrating the subject materials to students to help them understand programming concepts.',
                    'Designed assignments to identify the behavior of datasets in a Machine learning/Artificial Intelligence setting through the use of Weka, Pandas, and NumPy Python.'
                ]
            },
            {
                'title': 'Security Analyst',
                'organization': 'Ministry of Communications “Yesser” Egovernment Program',
                'dates': 'Sep 2015 - Oct 2016',
                'tasks': [
                    'Worked as a member of the Security Operations Center (SOC) team to detect, report, analyze, and mitigate security breaches through the use of Splunk SIEM, Nmap, and Nessus.',
                    'Coordinated a project for the “Bring Your Own Device” (BYOD) initiative to make use of employees’ devices to access the enterprise system in a secure and safe layer.',
                    'Participated in a penetration testing project to detect and disclose security vulnerabilities in Yesser’s infrastructure.',
                    'Created and executed unique test cases that address the basic functionality of several new features of the Yesser application.'
                ]
            },
        ],
        'education': [
            {
                'degree': 'Master of Science in Computer Science',
                'institution': 'New York University',
                'graduation': 'May 2025'
            },
            {
                'degree': 'Master of Science in Security Informatics',
                'institution': 'Johns Hopkins University',
                'graduation': 'May 2020',
                'gpa': '3.75/4.00'
            },
            {
                'degree': 'Bachelor of Science in Computer Information Systems',
                'institution': 'King Saud University',
                'graduation': 'Aug 2015',
                'gpa': '4.85/5.00'
            }
        ],
        'projects': [
            {
                'title': 'APT Attack Detection using AI',
                'organization': 'STC Chair for Artificial Intelligence',
                'dates': 'Jan 2021 - Jan 2022',
                'details': 'Researched and programed data extraction, modeling, and classification for APT attack detection using AI.'
            },
        ],
        'certifications': [
            {'name': 'CompTIA Cybersecurity Analyst (CySA+)', 'date': 'May 2021'},
            {'name': 'GIAC Penetration Tester (GPEN)', 'date': 'Oct 2021'},
        ],
        'publications': [
            {'title': 'The Accuracy of GPS‑Enabled Fitbit Activities as Evidence: A Digital Forensics Study', 'link': 'ieeexplore.ieee.org/document/9170981', 'date': 'Aug 2020'},
            {'title': 'Digital Forensic Analysis of Fitbit Wearable Technology: An Investigator’s Guide', 'link': 'ieeexplore.ieee.org/document/9170971', 'date': 'Aug 2020'},
        ]
    }
    return render(request, 'cv_app/index.html', context)
