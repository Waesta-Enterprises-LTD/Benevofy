from django.shortcuts import render, redirect

def view_administrators(request):
    admins = request.user.member.logged_in_association.admins.all()
    return render(request, 'benevofy/view_administrators.html', {'admins': admins})


def assign_admin(request, member_id):
    member = request.user.member
    new_admin = member.logged_in_association.members.get(id=member_id)
    member.logged_in_association.admins.add(new_admin)
    return redirect('administrators')


def revoke_admin(request, member_id):
    member = request.user.member
    admin = member.logged_in_association.members.get(id=member_id)
    member.logged_in_association.admins.remove(member)
    admin.current_mode = 'Member'
    admin.save()
    if admin == member:
        return redirect('member-dashboard')
    else:
        return redirect('administrators')
