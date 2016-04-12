from django import forms
import urllib2, json
from .models import SignUp, SearchLocation, GitSearch

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError("Please use a valid .edu email!")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

class SearchLocationForm(forms.ModelForm):
    location=[]

    class Meta:
        model = SearchLocation
        fields = ['city_name']


    def clean_city_name(self):
        city_name = self.cleaned_data.get('city_name')
        return city_name
    def search(self, city_name):
        url = 'http://maps.googleapis.com/maps/api/geocode/json?address='
        address = city_name.replace(' ', '%20')
        final_url = url + address + "&sensor=false"
        json_obj = urllib2.urlopen(final_url)
        data = json.load(json_obj)

        location = [data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng']]

        return location

class GitSearchForm(forms.ModelForm):
    followers = ""
    image = ""

    class Meta:
        model = GitSearch
        fields = ['user_name']

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        return user_name

    def gitSearch(self, user_name):
        url = 'https://api.github.com/users/'
        final_url = url + user_name
        json_obj = urllib2.urlopen(final_url)
        data = json.load(json_obj)


        if data['followers'] == 1:
            followers = [data['avatar_url'], "%s has %d follower on GitHub" %(user_name, data['followers'])]
            return followers

        followers =  [data['avatar_url'], "%s has %d followers on GitHub" %(user_name, data['followers'])]
        return followers
