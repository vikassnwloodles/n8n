1. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

You are a formatter. Convert the above updated template into a Slack Block Kit message using Block Kit JSON format.

Rules:
- Only use `"blocks"` format with `"section"` blocks and `"mrkdwn"` text.
- Do not include the original updated template.
- Do not include any explanation.
- Do not include any extra text.
- Respond with ONLY valid JSON starting with `{ "blocks": [` and ending with `] }`.


We are asking GPT to "Keep only modified template in your response...".
This can be the reason that it's including the modified template in the response as well.
And also we can try an option in n8n openai node to return response in json to get slack block json format. (We can't do that because getting folloing error when running the openai node by enabling `output content as json` option)
Bad request - please check your parameters
Invalid parameter: 'response_format' of type 'json_object' is not supported with this model.