import requests
import json

# Set up the SurveyMonkey API endpoint and authentication token
copy_endpoint = "https://api.surveymonkey.com/v3/surveys/{survey_id}/copy"
edit_endpoint = "https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions/{question_id}"
# Replace {access_token} with your actual access token
auth_token = "Bearer {access_token}"

# Set the survey ID of the survey you want to copy
# Replace with your actual survey ID
survey_id = "511470250"

# Set the number of copies you want to make
num_copies = 2

# Set the ID of the drop-down question you want to edit
question_id = "122931491"  # Replace with your actual question ID

# Set the new options for the drop-down question
new_options = ["Option 1", "Option 2", "Option 3"]

# Loop through the number of copies and make a copy of the survey each time
for i in range(num_copies):
    # Set the new survey title
    # Replace "My Survey" with the actual survey title
    new_title = f"Copy {i+1} of My Survey"

    # Set the payload for the copy survey request
    payload = {
        "from_survey_id": survey_id,
        "title": new_title,
        "nickname": new_title,
        "is_full_copy": True
    }

    # Make the copy survey request
    response = requests.post(copy_endpoint.format(survey_id=survey_id), headers={
                             "Authorization": auth_token}, json=payload)

    print(response)
    # Get the ID of the new survey
    new_survey_id = response.json()["id"]

    # Get the ID of the page containing the question you want to edit
    page_response = requests.get(
        f"https://api.surveymonkey.com/v3/surveys/{new_survey_id}/pages", headers={"Authorization": auth_token})
    # Assumes the first page contains the question you want to edit
    page_id = page_response.json()["data"][0]["id"]

    # Set the payload for the edit question request
    question_payload = {
        "headings": [],
        "family": "single_choice",
        "subtype": "vertical",
        "position": 1,
        "forced_ranking": False,
        "description": "",
        "options": [{"text": option} for option in new_options],
        "id": question_id
    }

    # Make the edit question request
    edit_response = requests.patch(edit_endpoint.format(survey_id=new_survey_id, page_id=page_id,
                                   question_id=question_id), headers={"Authorization": auth_token}, json=question_payload)

    # Print the response status code and body
    print(f"Copy {i+1}: Status Code {edit_response.status_code}")
    print(json.dumps(edit_response.json(), indent=2))
