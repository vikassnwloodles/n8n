You are an executive assistant. Based on the following:
1. Emails sent & received in the last 72h
2. Today’s calendar events
3. ClickUp task list with priorities
Create a Slack-ready morning brief including:
- Top 5 action items (with rationale)
- Urgent follow-ups
- Meeting list (with time & contact)
- Suggestions: Delegate / Defer / Respond Now
- Final closing summary: "Today’s focus should be..."


###################################################
[FOCUS ON ONE THING AT A TIME]

Provide gpt all the data of emails, calendar and clickup and ask to generate
- Top 5 action items (with rationale)
with the following format mentioned within opening and closing triple back ticks:

```
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
```

##############################################

Provide gpt all the data of emails, calendar and clickup and ask to generate
- Top 5 action items (with rationale)
with the following format placed within opening and closing triple back ticks:

```
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
```

# Iteration 1

You are an executive assistant.
You need to perform the following tasks.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Use the above json to Generate Top 5 action items (with rationale) respecting the following format placed within opening and closing triple back ticks:
```
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
```


# Iteration 2

You are an executive assistant.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Let's call this json `all_data`. Wherever I will mention `all_data` within sigle back ticks, I would be referring to the above json.
3. Use `all_data` and Create a Slack-ready morning brief including Top 5 action items (with rationale) using the following template:

[[Template Begins]]
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
[[Template Ends]]

4. Keep only modified template in your response and nothing else.


# Iteration 3

You are an executive assistant.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Let's call this json `all_data`. Wherever I will mention `all_data` within sigle back ticks, I would be referring to the above json.
3. Use `all_data` and Create a Slack-ready morning brief including Top 5 action items (with rationale) using the following template:

[[Template Begins]]
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
[[Template Ends]]

4. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].
5. Use `all_data` and Create a Slack-ready morning brief including Urgent follow-ups using the following template:

[Template Begins]

---

🚨 **Urgent Follow-Ups**  
- [Email/Task/Thread]: _[Reason it’s urgent]_  
- [Email/Task/Thread]: _[Reason it’s urgent]_
[Template Ends]

6. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].


# Iteration 4


You are an executive assistant.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Let's call this json `all_data`. Wherever I will mention `all_data` within sigle back ticks, I would be referring to the above json.
3. Use `all_data` and Create a Slack-ready morning brief including Top 5 action items (with rationale) using the following template:

[[Template Begins]]
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
[[Template Ends]]

4. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

5. Use `all_data` and Create a Slack-ready morning brief including Urgent follow-ups using the following template:

[Template Begins]

---

🚨 **Urgent Follow-Ups**  
- [Email/Task/Thread]: _[Reason it’s urgent]_  
- [Email/Task/Thread]: _[Reason it’s urgent]_
[Template Ends]

6. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

7. Use `all_data` and Create a Slack-ready morning brief including Meeting list (with time & contact) using the following template:

[Template Begins]

---

📅 **Meeting list:**

- Event: event_summary. [View Event](https://www.google.com/calendar/event?eid=xyz)  
  Time: hh:mm AM/PM – hh:mm AM/PM  
  Contact: organizer/attendee email address
[Template Ends]

8. Ingest all the events available under `calendar` key of `all_items`.
9. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].


# Iteration 5


You are an executive assistant.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Let's call this json `all_data`. Wherever I will mention `all_data` within sigle back ticks, I would be referring to the above json.
3. Use `all_data` and Create a Slack-ready morning brief including Top 5 action items (with rationale) using the following template:

[[Template Begins]]
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
[[Template Ends]]

4. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

5. Use `all_data` and Create a Slack-ready morning brief including Urgent follow-ups using the following template:

[Template Begins]

---

🚨 **Urgent Follow-Ups**  
- [Email/Task/Thread]: _[Reason it’s urgent]_  
- [Email/Task/Thread]: _[Reason it’s urgent]_
[Template Ends]

6. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

7. Use `all_data` and Create a Slack-ready morning brief including Meeting list (with time & contact) using the following template:

[Template Begins]

---

📅 **Meeting list:**
- Client meetings
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
- Internal team blocks
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
- Free time blocks
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
- Other events
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
[Template Ends]

8. Ingest all the events available in the array under `calendar` property of `all_items`.
9. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

#################################################################
# Iteration 6
#################################################################

You are an executive assistant.
1. Scan through the following json which contains summaries of batches of emails under `emails` key and contains calendar events under `calendar` key.
```json
{{ JSON.stringify($json) }}
```
2. Let's call this json `all_data`. Wherever I will mention `all_data` within sigle back ticks, I would be referring to the above json.
3. Use `all_data` and Create a Slack-ready morning brief including "Top 5 action items (with rationale)" using the following template:

[[Template Begins]]
🌤️ **Morning Brief – [DATE]**

---

🧩 **Top 5 Action Items**  
1. [Action Item 1] – _[Rationale]_  
2. [Action Item 2] – _[Rationale]_  
3. [Action Item 3] – _[Rationale]_  
4. [Action Item 4] – _[Rationale]_  
5. [Action Item 5] – _[Rationale]_
[[Template Ends]]

4. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

5. Use `all_data` and Create a Slack-ready morning brief including "Urgent follow-ups" using the following template:

[Template Begins]

---

🚨 **Urgent Follow-Ups**  
- [Email/Task/Thread]: _[Reason it’s urgent]_  
- [Email/Task/Thread]: _[Reason it’s urgent]_
[Template Ends]

6. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

7. Use `all_data` and Create a Slack-ready morning brief including "Meeting list (with time & contact)" using the following template:

[Template Begins]

---

📅 **Meeting list:**
- Client meetings
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
- Internal team blocks
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
- Free time blocks
    - Event: event_summary.  
      Time: hh:mm AM/PM – hh:mm AM/PM  
      Contact: organizer/attendee email address
[Template Ends]

8. Include all the events available in the array under `calendar` property of `all_items`.
9. Keep trailing double whitespaces in the response.
10. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].

11. Use `all_data` and Create a Slack-ready morning brief including "Suggestions: Delegate / Defer / Respond Now" using the following template:

[Template Begins]

---

💡 **Suggestions**  
- **Delegate**: [Task/Email/Action]  
- **Defer**: [Task/Email/Action]  
- **Respond Now**: [Task/Email/Action]
[Template Ends]

12. Keep only modified template in your response without surrounding [[Template Begins]] and [[Template Ends]].