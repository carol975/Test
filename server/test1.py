from server.models import UserProfiles, Skills, Types, Projects
from server.serializer import UsersSerializer, SkillsSerializer, UserProfilesSerializer, TypesSerializer, ProjectsSerializer
from rest_framework. renderers import JSONRenderer
from rest_framework.parsers import JSONParser

users = User

userprofiles = UserProfiles(user_summary='"Hello My name is Vincent"\n', location='"vancouver"\n', impage_path='"abcd@amazon.co.jp"\n')
userprofiles.save()
serializer = UserProfilesSerializer
serializer.data

skills = Skills(skill_name='"JAVA"\n')
skills.save()
serializer = SkillsSerializer
serializer.data

types = Types(type_name='"Mechanical"\n')
types.save()
serializer = TypesSerializer
serializer.data

projects = Projects(project_name='"Summer Project"\n', project_summary='"Un Project tres difficille pour moi"\n', image_path='"abcd@mamazon.jp"\n')
projects.save()
serializer = ProjectsSerializer
serializer.data

content = JSONRenderer().render(serializer.data)
content


