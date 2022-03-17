from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .models import Profile
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView, UpdateView, CreateView



class ProfileLogin(LoginView, View):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileLogin, self).get_context_data(*args, **kwargs)
        context['users'] = User.objects.all()
        return context

    def get_success_url(self):
      return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['bg', 'image', 'bio', 'inst']
    success_url = reverse_lazy('index')

class ProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/author.html'
    context_object_name = 'author'
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data()
        profile_posts = Post.objects.filter(archived=False, user=self.object.id)
        context['profile_posts'] = profile_posts
        return context

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

    # class FollowUnfollowView(APIView):
    #     permission_classes = [IsAuthenticated]
    #
    #     def current_profile(self):
    #         try:
    #             return Profile.objects.get(user=self.request.user)
    #         except Profile.DoesNotExist:
    #             raise Http404
    #
    #     def other_profile(self, pk):
    #         try:
    #             return Profile.objects.get(id=pk)
    #         except Profile.DoesNotExist:
    #             raise Http404
    #
    #     def post(self, request, format=None):
    #
    #         pk = request.data.get('id')  # Here pk is opposite user's profile ID
    #         req_type = request.data.get('type')
    #
    #         current_profile = self.current_profile()
    #         other_profile = self.other_profile(pk)
    #
    #         if req_type == 'follow':
    #             if other_profile.private_account:
    #                 other_profile.panding_request.add(current_profile)
    #                 return Response({"Requested": "Follow request has been send!!"}, status=status.HTTP_200_OK)
    #             else:
    #                 if other_profile.blocked_user.filter(id=current_profile.id).exists():
    #                     return Response({
    #                                         "Following Fail": "You can not follow this profile becuase your ID blocked by this user!!"},
    #                                     status=status.HTTP_400_BAD_REQUEST)
    #                 current_profile.following.add(other_profile)
    #                 other_profile.followers.add(current_profile)
    #                 return Response({"Following": "Following success!!"}, status=status.HTTP_200_OK)
    #
    #         elif req_type == 'accept':
    #             current_profile.followers.add(other_profile)
    #             other_profile.following.add(current_profile)
    #             current_profile.panding_request.remove(other_profile)
    #             return Response({"Accepted": "Follow request successfuly accespted!!"}, status=status.HTTP_200_OK)
    #
    #         elif req_type == 'decline':
    #             current_profile.panding_request.remove(other_profile)
    #             return Response({"Decline": "Follow request successfully declined!!"}, status=status.HTTP_200_OK)
    #
    #         elif req_type == 'unfollow':
    #             current_profile.following.remove(other_profile)
    #             other_profile.followers.remove(current_profile)
    #             return Response({"Unfollow": "Unfollow success!!"}, status=status.HTTP_200_OK)
    #
    #         elif req_type == 'remove':  # You can remove your follower
    #             current_profile.followers.remove(other_profile)
    #             other_profile.following.remove(current_profile)
    #             return Response({"Remove Success": "Successfuly removed your follower!!"}, status=status.HTTP_200_OK)
    #
    #     # Here we can fetch followers,following detail and blocked user,pending request,sended request..
    #
    #     def patch(self, request, format=None):
    #
    #         req_type = request.data.get('type')
    #
    #         if req_type == 'follow_detail':
    #             serializer = FollowerSerializer(self.current_profile())
    #             return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    #
    #         elif req_type == 'block_pending':
    #             serializer = BlockPendinSerializer(self.current_profile())
    #             pf = list(
    #                 Profile.objects.filter(panding_request=self.current_profile().id).values('id', 'user__username',
    #                                                                                          'profile_pic',
    #                                                                                          'overall_pr'))
    #             return Response({"data": serializer.data, "Sended Request": pf}, status=status.HTTP_200_OK)
    #
    #     # You can block and unblock user
    #
    #     def put(self, request, format=None):
    #         pk = request.data.get('id')  # Here pk is oppisite user's profile ID
    #         req_type = request.data.get('type')
    #
    #         if req_type == 'block':
    #             self.current_profile().blocked_user.add(self.other_profile(pk))
    #             return Response({"Blocked": "This user blocked successfuly"}, status=status.HTTP_200_OK)
    #         elif req_type == 'unblock':
    #             self.current_profile().blocked_user.remove(self.other_profile(pk))
    #             return Response({"Unblocked": "This user unblocked successfuly"}, status=status.HTTP_200_OK)
