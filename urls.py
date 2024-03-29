""" URLConf """


from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views

from portfolio.forms.main import *
from portfolio.views.main import *

app_name = 'portfolio'

urlpatterns = [
    # Main views
    # path('', IndexView.as_view(), name='index'),
    path(
        '',
        PublicSkillListView.as_view(),
        name='index'
    ),
    path(
        'about/',
        AboutView.as_view(),
        name='about'
    ),
    path(
        'contact/',
        ContactView.as_view(),
        name='contact'
    ),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),

    # Public views
    path(
        'badge/',
        PublicBadgeListView.as_view(),
        name='public_badge_list'
    ),
    path(
        'project/',
        PublicProjectListView.as_view(),
        name='public_project_list'
    ),
    path(
        'certificate/',
        PublicCertificateListView.as_view(),
        name='public_certificate_list'
    ),

    # Providers
    path(
        'providers/',
        ProviderListView.as_view(),
        name='provider_list'
    ),
    path(
        'providers/new/',
        ProviderCreateView.as_view(),
        name='create_provider'
    ),
    path(
        'providers/<int:pk>/edit/',
        ProviderUpdateView.as_view(),
        name='edit_provider'
    ),
    path(
        'providers/<int:pk>/delete/',
        ProviderDeletionView.as_view(),
        name='delete_provider'
    ),

    # Tags
    path(
        'tags/',
        TagListView.as_view(),
        name='tag_list'
    ),
    path(
        'tags/new/',
        TagCreateView.as_view(),
        name='create_tag'
    ),
    path(
        'tags/<int:pk>/edit/',
        TagUpdateView.as_view(),
        name='edit_tag'
    ),
    path(
        'tags/<int:pk>/delete/',
        TagDeletionView.as_view(),
        name='delete_tag'
    ),

    # Certificates
    path(
        'certificates/',
        CertificateListView.as_view(),
        name='certificate_list'
    ),
    path(
        'certificates/new/',
        CertificateCreateView.as_view(),
        name='create_certificate'
    ),
    path(
        'certificates/<int:pk>/edit/',
        CertificateUpdateView.as_view(),
        name='edit_certificate'
    ),
    path(
        'certificates/<int:pk>/delete/',
        CertificateDeletionView.as_view(),
        name='delete_certificate'
    ),

    # Badges
    path(
        'badges/',
        BadgeListView.as_view(),
        name='badge_list'
    ),
    path(
        'badges/new/',
        BadgeCreateView.as_view(),
        name='create_badge'
    ),
    path(
        'badges/<int:pk>/edit/',
        BadgeUpdateView.as_view(),
        name='edit_badge'
    ),
    path(
        'badges/<int:pk>/delete/',
        BadgeDeletionView.as_view(),
        name='delete_badge'
    ),

    # Projects
    path(
        'projects/',
        ProjectListView.as_view(),
        name='project_list'
    ),
    path(
        'projects/new/',
        ProjectCreateView.as_view(),
        name='create_project'
    ),
    path(
        'projects/<int:pk>/edit/',
        ProjectUpdateView.as_view(),
        name='edit_project'
    ),
    path(
        'projects/<int:pk>/delete/',
        ProjectDeletionView.as_view(),
        name='delete_project'
    ),
    path(
        'projects/<int:pid>/image/',
        ModelImageView.as_view(model=Project),
        name='project_image'
    ),

    # Messages
    path(
        'messages/',
        MessageListView.as_view(),
        name='message_list'
    ),
    path(
        'message/',
        MessageCreateView.as_view(),
        name='send_message'
    ),
    path(
        'messages/<int:pk>/delete/',
        MessageDeletionView.as_view(),
        name='delete_message'
    ),

    # Skills
    path(
        'skills/',
        SkillListView.as_view(),
        name='skill_list'
    ),
    path(
        'skills/new/',
        SkillCreateView.as_view(),
        name='create_skill'
    ),
    path(
        'skills/<int:pk>/edit/',
        SkillUpdateView.as_view(),
        name='edit_skill'
    ),
    path(
        'skills/<int:pk>/delete/',
        SkillDeletionView.as_view(),
        name='delete_skill'
    ),
] + [
    # Custom Authentication
    path(
        'accounts/login/',
        views.LoginView.as_view(
            form_class=StyledAuthenticationForm,
            template_name='portfolio/authentication/login.html',
            extra_context={
                'signup_form': StyledUserCreationForm()
            }
        ),
        name='login'
    ),
    path(
        'accounts/register/',
        UserCreateView.as_view(),
        name='register'
    ),
    path(
        'accounts/<int:pk>/edit/',
        UserUpdateView.as_view(),
        name='edit_user'
    ),
    path(
        'accounts/<int:pk>/delete/',
        UserDeletionView.as_view(),
        name='delete_user'
    ),
    path(
        'accounts/logout/',
        views.LogoutView.as_view(
            template_name='portfolio/authentication/logged_out.html'
        ),
        name='logout'
    ),
    path(
        'accounts/profile/',
        ProfileView.as_view(),
        name='profile'
    ),
    path(
        'accounts/password/change/',
        views.PasswordChangeView.as_view(
            form_class=StyledPasswordChangeForm,
            template_name='portfolio/authentication/change_password.html',
            success_url=reverse_lazy('portfolio:change_done')
        ),
        name='change_password'
    ),
    path(
        'accounts/password/change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='portfolio/authentication/change_done.html'
        ),
        name='change_done'
    ),
    path(
        'accounts/password/reset/',
        views.PasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name='portfolio/authentication/reset_password.html',
            success_url=reverse_lazy('portfolio:reset_done')
        ),
        name='reset_password'
    ),
    path(
        'accounts/password/reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='portfolio/authentication/reset_done.html'
        ),
        name='reset_done'
    ),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='portfolio/authentication/reset_confirm.html',
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy('portfolio:reset_complete')
        ),
        name='reset_confirm'
    ),
    path(
        'accounts/password/reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='portfolio/authentication/reset_complete.html',
        ),
        name='reset_complete'
    ),
]
