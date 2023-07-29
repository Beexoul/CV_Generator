    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

    def create_cv_pdf(output_file, personal_info, objective, education, work_experience, skills, projects,
                    certifications, publications, awards, interests):
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Content for the PDF
        content = []
        
        # Personal Information
        content.append(Paragraph("<b>Personal Information:</b>", styles['Heading1']))
        for info in personal_info:
            content.append(Paragraph(info, styles['Normal']))
        
        # Objective or Personal Statement
        if objective:
            content.append(Paragraph("<b>Objective or Personal Statement:</b>", styles['Heading1']))
            content.append(Paragraph(objective, styles['Normal']))
        
        # Education
        content.append(Paragraph("<b>Education:</b>", styles['Heading1']))
        for edu in education:
            content.append(Paragraph(edu, styles['Normal']))
        
        # Work Experience
        content.append(Paragraph("<b>Work Experience:</b>", styles['Heading1']))
        for exp in work_experience:
            content.append(Paragraph(exp, styles['Normal']))
        
        # Skills
        content.append(Paragraph("<b>Skills:</b>", styles['Heading1']))
        for skill in skills:
            content.append(Paragraph(skill, styles['Normal']))
        
        # Projects (optional)
        if projects:
            content.append(Paragraph("<b>Projects:</b>", styles['Heading1']))
            for project in projects:
                content.append(Paragraph(project, styles['Normal']))
        
        # Certifications and Training (optional)
        if certifications:
            content.append(Paragraph("<b>Certifications and Training:</b>", styles['Heading1']))
            for cert in certifications:
                content.append(Paragraph(cert, styles['Normal']))
        
        # Publications (optional)
        if publications:
            content.append(Paragraph("<b>Publications:</b>", styles['Heading1']))
            for pub in publications:
                content.append(Paragraph(pub, styles['Normal']))
        
        # Awards and Honors (optional)
        if awards:
            content.append(Paragraph("<b>Awards and Honors:</b>", styles['Heading1']))
            for award in awards:
                content.append(Paragraph(award, styles['Normal']))
        
        # Interests and Hobbies (optional)
        if interests:
            content.append(Paragraph("<b>Interests and Hobbies:</b>", styles['Heading1']))
            for interest in interests:
                content.append(Paragraph(interest, styles['Normal']))
        
        # Build the PDF
        doc.build(content)

    if __name__ == "__main__":
        output_file = "my_cv.pdf"  # Change the file name if desired
        
        # Get user input for each section
        personal_info = []
        personal_info.append(input("Enter your full name: "))
        personal_info.append(input("Enter your email: "))
        personal_info.append(input("Enter your phone number: "))
        # Add optional personal info fields here (date of birth, nationality, etc.)
        # Example:
        # personal_info.append(input("Enter your date of birth: "))
        # personal_info.append(input("Enter your nationality: "))
        # personal_info.append(input("Enter your LinkedIn profile link: "))
        
        objective = input("Enter your objective or personal statement (optional): ")
        
        education = []
        while True:
            edu = input("Enter educational qualifications (enter 'done' when finished): ")
            if edu.lower() == 'done':
                break
            education.append(edu)
        
        work_experience = []
        while True:
            exp = input("Enter work experience (enter 'done' when finished): ")
            if exp.lower() == 'done':
                break
            work_experience.append(exp)
        
        skills = []
        while True:
            skill = input("Enter a skill (enter 'done' when finished): ")
            if skill.lower() == 'done':
                break
            skills.append(skill)
        
        projects = []
        while True:
            project = input("Enter a project (enter 'done' when finished, leave empty if none): ")
            if project.lower() == 'done':
                break
            projects.append(project)
        
        certifications = []
        while True:
            cert = input("Enter a certification or training (enter 'done' when finished, leave empty if none): ")
            if cert.lower() == 'done':
                break
            certifications.append(cert)
        
        publications = []
        while True:
            pub = input("Enter a publication (enter 'done' when finished, leave empty if none): ")
            if pub.lower() == 'done':
                break
            publications.append(pub)
        
        awards = []
        while True:
            award = input("Enter an award or honor (enter 'done' when finished, leave empty if none): ")
            if award.lower() == 'done':
                break
            awards.append(award)
        
        interests = []
        while True:
            interest = input("Enter an interest or hobby (enter 'done' when finished, leave empty if none): ")
            if interest.lower() == 'done':
                break
            interests.append(interest)
        
        create_cv_pdf(output_file, personal_info, objective, education, work_experience, skills, projects,
                    certifications, publications, awards, interests)
        print(f"CV generated and saved as {output_file}")
