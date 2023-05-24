#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Hello")


# In[ ]:


QUESTIONS = [
    'Do you need a general check-up?',
    'Do you require a specialist consultation?',
    'Do you need diagnostic tests?',
    'Do you require any surgeries?',
    'Are you experiencing any specific symptoms or conditions?',
    'Do you need assistance with medication management?'
]

THRESHOLD = {
    'Basic': 3,
    'Intermediate': 6,
    'Advanced': 9
}

SERVICES = {
    'General Check-up': ['Physical examination', 'Routine blood tests', 'Vaccinations'],
    'Specialist Consultation': ['Cardiology', 'Dermatology', 'Orthopedics', 'Gynecology', 'Neurology'],
    'Diagnostic Tests': ['X-ray', 'MRI', 'CT scan', 'Blood tests'],
    'Surgeries': ['Cataract surgery', 'Knee replacement', 'Hernia repair'],
    'Medication Management': ['Prescription refill', 'Medication counseling', 'Dosage adjustment'],
}

def expertSystem(questions, threshold, services):
    score = 0
    for question in questions:
        print(question + " (Y/N)")
        ans = input("> ")
        if ans.lower() == 'y':
            score += 1
        print()
        print()

    if score >= threshold['Advanced']:
        print("Based on your responses, you require ADVANCED medical facilities.")
        print("We recommend contacting a specialized hospital or medical center that can cater to your specific needs.")
        recommend_services(services)
    elif score >= threshold['Intermediate']:
        print("Based on your responses, you require INTERMEDIATE medical facilities.")
        print("We suggest seeking assistance from a comprehensive medical facility that offers a wide range of services.")
        recommend_services(services)
    elif score >= threshold['Basic']:
        print("Based on your responses, you require BASIC medical facilities.")
        print("You can visit a general hospital or clinic to address your healthcare needs.")
        recommend_services(services)
    else:
        print("Based on your responses, you have minimal requirements for medical facilities.")
        print("You may consider visiting a local clinic or consulting a primary care physician.")

def recommend_services(services):
    print("Here are some services that may be relevant to your needs:")
    for service, sub_services in services.items():
        print(service + ":")
        for sub_service in sub_services:
            print("- " + sub_service)
        print()

if __name__ == '__main__':
    print("\n\n\t\tWelcome To The Hospital and Medical Facilities EXPERT SYSTEM\n")
    print("\tNote: Please answer the following questions honestly to determine your medical facility needs\n\n")
    expertSystem(QUESTIONS, THRESHOLD, SERVICES)


# In[ ]:




