{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": {{ JSON.stringify($json.choices[0].message.content) }}
      }
    }
  ]
}
