from Menu import Menu
from Option import Option
from constants import *
"""
This little file just has the menus declared.  Each variable (e.g. menu_main) has 
its own set of options and actions.  Although, you'll see that the "action" could
be something other than an operation to perform.

Doing the menu declarations here seemed like a cleaner way to define them.  When
this is imported in main.py, these assignment statements are executed and the 
variables are constructed.  To be honest, I'm not sure whether these are global
variables or not in Python.
"""
enroll_menu = Menu("Enroll/Unenroll", "Choose an option:", [
    #enroll student to section AND section to student
    Option("Enroll a Student in a Section", "enroll_student_to_section(sess)"),
    Option("Enroll a Section to Student", "enroll_section_to_student(sess)"),

    #unenroll student from section AND section to student
    Option("Unenroll a Student from a Section", "unenroll_student_from_section(sess)"),
    Option("Unenroll a Section from a Student", "unenroll_section_from_student(sess)"),



    Option("Exit", "pass")
])

list_enrollments_menu = Menu("List Enrollments", "Choose an option:", [
    #list enrollments by section AND list enrollmetns by student
    Option("List enrollments by selecting a Student", "list_student_enrollments(sess)"),
    Option("List enrollments by selecting a Section", "list_section_enrollments(sess)"),


    Option("Exit", "pass")
])


# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add(sess)"),
    Option("List", "list_objects(sess)"),
    Option("Delete", "delete(sess)"),
    Option("Boilerplate Data", "boilerplate(sess)"),
    Option("Commit", "sess.commit()"),
    Option("Rollback", "session_rollback(sess)"),
    #Option("Enroll and/or Unenroll", "enroll_menu"),
    #Option("List Enrollments", "list_enrollments_menu"),
    Option("Exit this application", "pass")

])

add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Department", "add_department(sess)"),
    Option("Course", "add_course(sess)"),
    Option("Major", "add_major(sess)"),
    Option("Student", "add_student(sess)"),
    Option("Student to Major", "add_student_major(sess)"),
    Option("Major to Student", "add_major_student(sess)"),
    Option("Section","add_section(sess)"),
    Option("Enroll a Student in a Section", "enroll_student_to_section(sess)"),
    Option("Enroll a Section to Student", "enroll_section_to_student(sess)"),
    Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
    Option("Department", "delete_department(sess)"),
    Option("Course", "delete_course(sess)"),
    Option("Major", "delete_major(sess)"),
    Option("Student", "delete_student(sess)"),
    Option("Student to Major", "delete_student_major(sess)"),
    Option("Major to Student", "delete_major_student(sess)"),
    Option("Unenroll a Student from a Section", "unenroll_student_from_section(sess)"),
    Option("Unenroll a Section from a Student", "unenroll_section_from_student(sess)"),
    Option("Section", "delete_section(sess)"), #TO DELETE A SECTION

    Option("Exit", "pass")
])

list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("Department", "list_department(sess)"),
    Option("Course", "list_course(sess)"),
    Option("Major", "list_major(sess)"),
    Option("Student", "list_student(sess)"),
    Option("Student to Major", "list_student_major(sess)"),
    Option("Major to Student", "list_major_student(sess)"),
    Option("List enrollments by selecting a Student", "list_student_enrollments(sess)"),
    Option("List enrollments by selecting a Section", "list_section_enrollments(sess)"),
    Option("Section","list_sections(sess)"),
    Option("Exit", "pass")
])

# A menu to prompt for the amount of logging information to go to the console.
debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
])

# A menu to prompt for whether to create new tables or reuse the old ones.
introspection_select = Menu("introspection selectt", 'To introspect or not:', [
    Option('Start all over', START_OVER),
#   Option("Reuse tables", INTROSPECT_TABLES),
    Option("Reuse without introspection", REUSE_NO_INTROSPECTION)
])
