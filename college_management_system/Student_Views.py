from django.shortcuts import render,redirect
from app.models import Student_Notification,Student,Student_Feedback
from django.contrib import messages


def HOME(request):
    return render(request,'Student/home.html')

def STUDENT_NOTIFICATION(request):

    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification': notification,
        }

    return render(request,'Student/notification.html',context)



def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')


def STUDENT_FEEDBACK(request):
    return render(request,'Student/feedback.html')

def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)

        feedbacks = Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = ""
        )
        feedbacks.save()
        messages.success(request,'Feedback are Successfully Sent')
        
        return redirect('student_feedback')