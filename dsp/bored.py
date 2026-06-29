from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import inch

pdf_path = "/mnt/data/MBA_Entrance_Exams_UserFriendly.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()

title_style = styles["Title"]
section_style = styles["Heading2"]
normal = styles["Normal"]

story = []

story.append(Paragraph("MBA Entrance Exams in India (2025–2026)", title_style))
story.append(Spacer(1, 12))

sections = [
    ("1️⃣ CMAT 2026 (Best for Low–Medium Budget)",
     [
         "Exam Date: April 2026",
         "Difficulty: Easy–Moderate",
         "Fees: ₹3–8 lakhs",
         "Course Duration: 2 years",
         "Top Colleges: JBIMS, PUMBA, KJ Somaiya, Great Lakes, BIMTECH, Welingkar",
         "Why Choose: Affordable + many government colleges"
     ]),
    ("2️⃣ MAT (Easy & conducted many times yearly)",
     [
         "Exam Dates: Feb, May, Sept, Dec sessions",
         "Difficulty: Easy",
         "Fees: ₹4–9 lakhs",
         "Course Duration: 2 years",
         "Top Colleges: Christ University, VIT, IPE Hyderabad, IBA Bangalore",
         "Why Choose: Very easy exam + multiple attempts"
     ]),
    ("3️⃣ SNAP 2025",
     [
         "Exam Date: December 2025",
         "Difficulty: Moderate",
         "Fees: ₹6–12 lakhs",
         "Course Duration: 2 years",
         "Top Colleges: SIBM Pune, SCMHRD, SIOM, SIMS",
         "Why Choose: 1-hour exam, top private B-schools"
     ]),
    ("4️⃣ NMAT 2025",
     [
         "Exam Window: Until December 2025",
         "Difficulty: Moderate",
         "Fees: ₹10–20 lakhs",
         "Course Duration: 2 years",
         "Top Colleges: NMIMS Mumbai, XUB, ICFAI",
         "Why Choose: Retake options + adaptive test"
     ])
]

for title, bullets in sections:
    story.append(Paragraph(title, section_style))
    story.append(ListFlowable(
        [ListItem(Paragraph(b, normal)) for b in bullets],
        bulletType="bullet"
    ))
    story.append(Spacer(1, 12))

doc.build(story)
pdf_path
