from orm_base import Base
from sqlalchemy import Integer, UniqueConstraint, ForeignKeyConstraint, Column, Identity
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from Student import Student
from Section import Section
from Course import Course

class Enrollment(Base):
    '''This is the association between student and section. It allows a student to join a section
    and leave it'''

    __tablename__ = "enrollments"
    student: Mapped["Student"] = relationship(back_populates = "sections")
    section: Mapped["Section"] = relationship(back_populates = "students")
    studentId: Mapped[int] = mapped_column("student_id", Integer, Identity(start=1, cycle=True), primary_key=True)
    sectionNumber: Mapped[int] = mapped_column("section_number", Integer, Identity(start=1, cycle=True),
                                               nullable=False, primary_key=True)
    courseNumber: Mapped[int] = mapped_column("course_number", nullable=False, primary_key=True)
    #course: Mapped["Course"] = relationship(back_populates="sections")
    semester: Mapped[str] = mapped_column("semester", String(10), nullable=False, primary_key=True)
    sectionYear: Mapped[int] = mapped_column("section_year", Integer, nullable=False, primary_key=True)
    departmentAbbreviation: Mapped[str] = mapped_column("department_abbreviation", nullable=False, primary_key=True)


    __table_args__ = (UniqueConstraint("student_id","department_abbreviation","course_number","section_number","section_year","semester", name =
                                       "enrollments_uk_01"),
                      ForeignKeyConstraint([departmentAbbreviation, courseNumber, sectionNumber, sectionYear, semester],
                                           ["sections.department_abbreviation", "sections.course_number",
                                            "sections.section_number","sections.section_year", "sections.semester"]),
                      ForeignKeyConstraint([studentId], ["students.student_id"]))

    def __int__(self, student, section):
        self.student = student
        self.studentId = student.studentID
        self.section = section
        self.sectionNumber = section.sectionNumber
        self.sectionYear = section.sectionYear
        self.courseNumber = section.courseNumber
        self.semester = section.semester
        self.departmentAbbreviation = section.departmentAbbreviation


    def __str__(self):
            return f"Enrollment - studentId: {self.studentId} sectionNumber: {self.sectionNumber} semester: {self.semester} "