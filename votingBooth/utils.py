import openai
import re
import ast


def GenerateGPTResponse(prompt):
        try:
            # Check if the input text is not empty
            if not prompt:
                raise "Input text is required"
             

            # Call the OpenAI GPT-3 API
            client = openai.OpenAI(
                # This is the default and can be omitted
                api_key="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",
            )
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )

            # Extract the generated response
            generated_response = response.choices[0].message.content

            return generated_response

        except Exception as e:
            print(e)
          

def getVotterandGardian(text):
    pattern = r"\{[^{}]*\}"

    # Find the dictionary using regex
    match = re.search(pattern, text)

    if match:
        # Extract the dictionary string
        dictionary_str = match.group(0)
        
        # Convert the dictionary string to a Python dictionary safely
        try:
            dictionary = ast.literal_eval(dictionary_str)
        except ValueError:
            print("Invalid dictionary string.")
            dictionary = {}
        
        # Get the values from the dictionary
        values = list(dictionary.values())
        return values
    else:
        print("No dictionary found in the text.")
        return ["not set","not set"]