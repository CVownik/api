import pytest
from users.models import CustomUser
from cv.models import (
    CV,
    CVInfo,
    Contact,
    ContactLinks,
    Experience,
    Duties,
    Education,
    Languages,
    Interests,
    SoftSkills,
    HardSkills,
    Projects,
)
import datetime

# Test User Creation


@pytest.fixture
def create_user():

    return CustomUser.object.create_user(
        email="test@example.com",
        password="testpassword123",
        name="Jan",
        surname="Kowalski",
        hr_role=False,
        premium_role=False,
        is_active=True,
        is_staff=False,
        is_superuser=False,
        trial_used_hr=False,
    )


# Test CV Creation
@pytest.fixture
def create_cv(create_user):
    user = create_user
    return CV.objects.create(
        user_id=user,
        created_at=datetime.datetime.now(),
    )

# Test CVInfo Creation


@pytest.fixture
def create_cv_info(create_user):
    return CVInfo.objects.create(
        userId=create_user,
        name="Ewa",
        surname="Kowalska",
        about="Software Developer z 10-letnim doświadczeniem w branży IT.",
        avatar=None,
        thumbnail=None,
        created_at=datetime.datetime.now(),
    )


# Test Contact Creation


@pytest.fixture
def create_contact(create_cv_info):
    cv_info = create_cv_info
    return Contact.objects.create(
        cv_info_id=cv_info,
        telephone="623123412",
        email="janKowal@example.com",
        city="Warszawa",
    )


# Test Experience Creation


@pytest.fixture
def create_experience(create_cv_info):
    cv_info = create_cv_info
    return Experience.objects.create(
        cv_info_id=cv_info,
        position="Software Engineer",
        company="WebTechnic",
        location="Warszawa",
        start_date=datetime.date(2015, 1, 1),
        end_date=datetime.date(2020, 12, 31),
    )


# Test CVModels


@pytest.mark.django_db
class TestCVModels:
    
    def test_create_cv(self, create_user):
        user = create_user
        cv = CV.objects.create(
            userId=user,
            created_at=datetime.datetime.now(),
        )
        assert cv.userId == user
        assert cv.created_at is not None
    
    def test_create_cv_info(self, create_cv):
        cv = create_cv
        cv_info = CVInfo.objects.create(
            cv_id=cv,
            name="Jan",
            surname="Kowalski",
            about="Software Developer z 5-letnim doświadczeniem w branży IT.",
            avatar=None,
            thumbnail=None,
            created_at=datetime.datetime.now(),
        )
        assert cv_info.cv_id == cv
        assert cv_info.name == "Jan"
        assert cv_info.surname == "Kowalski"
        assert (
            cv_info.about == "Software Developer z 5-letnim doświadczeniem w branży IT."
        )
        assert not cv_info.avatar
        assert not cv_info.thumbnail
        assert cv_info.created_at is not None

    def test_create_contact(self, create_cv_info):
        cv_info = create_cv_info
        contact = Contact.objects.create(
            cv_info_id=cv_info,
            telephone="623123412",
            email="janKowal@gmail.com",
            city="Warszawa",
        )
        assert contact.cv_info_id == cv_info
        assert contact.telephone == "623123412"
        assert contact.email == "janKowal@gmail.com"
        assert contact.city == "Warszawa"

    def test_create_contact_links(self, create_contact):
        contact = create_contact
        contact_link = ContactLinks.objects.create(
            contact_id=contact,
            name="LinkedIn",
            link="https://www.linkedin.com/in/jankowalski/",
        )

        assert contact_link.contact_id == contact
        assert contact_link.name == "LinkedIn"
        assert contact_link.link == "https://www.linkedin.com/in/jankowalski/"

    def test_create_experience(self, create_cv):
        cv = create_cv
        experience = Experience.objects.create(
            cv_id=cv,
            position="Software Engineer",
            company="Januszex",
            location="Olsztyn",
            start_date=datetime.date(2015, 1, 1),
            end_date=datetime.date(2020, 12, 31),
        )

        assert experience.cv_id == cv
        assert experience.position == "Software Engineer"
        assert experience.company == "Januszex"
        assert experience.location == "Olsztyn"
        assert experience.start_date == datetime.date(2015, 1, 1)
        assert experience.end_date == datetime.date(2020, 12, 31)

    def test_create_duties(self, create_experience):
        experience = create_experience
        duty = Duties.objects.create(
            experience_id=experience,
            description="Rozwój i utrzymanie aplikacji webowych przy użyciu Django i React.",
        )

        assert duty.experience_id == experience
        assert (
            duty.description
            == "Rozwój i utrzymanie aplikacji webowych przy użyciu Django i React."
        )

    def test_create_duties2(self, create_experience):
        experience = create_experience
        duty = Duties.objects.create(
            experience_id=experience,
            description="Prowadzenie zespołu programistów w celu dostarczenia wysokiej jakości rozwiązań programowych.",
        )

        assert duty.experience_id == experience
        assert (
            duty.description
            == "Prowadzenie zespołu programistów w celu dostarczenia wysokiej jakości rozwiązań programowych."
        )

    def test_create_education(self, create_cv):
        cv = create_cv
        education = Education.objects.create(
            cv_id=cv,
            institution="Uniwersytet Mikolaja Kopernika w Toruniu",
            degree="Inżynier",
            start_date=datetime.date(2010, 9, 1),
            end_date=datetime.date(2014, 6, 30),
        )

        assert education.cv_id == cv
        assert education.institution == "Uniwersytet Mikolaja Kopernika w Toruniu"
        assert education.degree == "Inżynier"
        assert education.start_date == datetime.date(2010, 9, 1)
        assert education.end_date == datetime.date(2014, 6, 30)

    def test_create_languages(self, create_cv):
        cv = create_cv
        language = Languages.objects.create(
            cv_id=cv,
            language="Angielski",
            language_lever="B2",
        )

        assert language.cv_id == cv
        assert language.language == "Angielski"
        assert language.language_lever == "B2"

    def test_create_interests(self, create_cv):
        cv = create_cv
        interest = Interests.objects.create(
            cv_id=cv,
            interest="Nurkowanie",
        )
        assert interest.cv_id == cv
        assert interest.interest == "Nurkowanie"

    def test_create_interests2(self, create_cv):
        cv = create_cv
        interest = Interests.objects.create(
            cv_id=cv,
            interest="Programowanie w Pythonie",
        )
        assert interest.cv_id == cv
        assert interest.interest == "Programowanie w Pythonie"

    def test_create_soft_skills(self, create_cv):
        cv = create_cv
        soft_skill = SoftSkills.objects.create(
            cv_id=cv,
            skill="Komunikacja interpersonalna",
        )
        assert soft_skill.cv_id == cv
        assert soft_skill.skill == "Komunikacja interpersonalna"

    def test_create_soft_skills2(self, create_cv):
        cv = create_cv
        soft_skill = SoftSkills.objects.create(
            cv_id=cv,
            skill="Odporność na stres",
        )
        assert soft_skill.cv_id == cv
        assert soft_skill.skill == "Odporność na stres"

    def test_create_hard_skills(self, create_cv):
        cv= create_cv
        hard_skill = HardSkills.objects.create(
            cv_id=cv,
            skill="Znajomość Python: biblioteki Django, numpy, Pandas, pytest",
        )
        assert hard_skill.cv_id == cv
        assert (
            hard_skill.skill
            == "Znajomość Python: biblioteki Django, numpy, Pandas, pytest"
        )

    def test_create_hard_skills2(self, create_cv):
        cv = create_cv
        hard_skill = HardSkills.objects.create(
            cv_id=cv,
            skill="Znajomość JavaScript: biblioteki React, json, API",
        )
        assert hard_skill.cv_id == cv
        assert hard_skill.skill == "Znajomość JavaScript: biblioteki React, json, API"

    def test_create_projects(self, create_cv):
        cv = create_cv
        project = Projects.objects.create(
            cv_id=cv,
            name="ProjectApp",
            description="Aplikacja webowa do zarządzania projektami z wykorzystaniem Django i React oraz Gaussian Splattingu.",
            start_date=datetime.date(2021, 1, 1),
            end_date=datetime.date(2021, 12, 31),
        )
        assert project.cv_id == cv
        assert project.name == "ProjectApp"
        assert (
            project.description
            == "Aplikacja webowa do zarządzania projektami z wykorzystaniem Django i React oraz Gaussian Splattingu."
        )
        assert project.start_date == datetime.date(2021, 1, 1)
        assert project.end_date == datetime.date(2021, 12, 31)
