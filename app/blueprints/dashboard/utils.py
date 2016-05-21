from app.models import db
from app.models.user import User
from app.models.skill import Skill
from app.models.role import Role 

def matching_companies(user):
        """
        Returns a list of matching companiesordered by relevance
        """
        user_skills = user._user_skills_as_set

        companies = db.session.query(User)\
                    .join(User.roles)\
                    .filter(Role.name=="company").all()
       
        matching_companies = []
        for company in companies:
         
            
            company_skills = set([skill.id for skill in company.skills])
            match_skills = [skill for skill in user_skills & company_skills]
            other_skills = [skill for skill in company_skills - user_skills]
           
            if len(match_skills) > 0:

                # Model lists
                match_skills_obj = [
                    db.session.query(Skill).get(skill) for skill in match_skills]
                other_skills_obj = [
                    db.session.query(Skill).get(skill) for skill in other_skills]

                match = {
                    "model": company,
                    "matches": len(match_skills),
                    "skills": match_skills_obj,
                    "other_skills": other_skills_obj
                }
                matching_companies.append(match)

        # sort the list by matches, most matches first
        from operator import itemgetter
        sorted_matching_companies = sorted(matching_companies,
                                           key=itemgetter('matches'),
                                           reverse=True)
        return sorted_matching_companies