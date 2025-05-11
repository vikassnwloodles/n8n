| Key           | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| from          | The sender's email address.                                                 |
| to            | The primary recipient(s) of the email.                                      |
| cc            | Carbon copy recipients who also received the email.                         |
| references    | Message IDs of previous related emails in the thread, used for threading.   |
| replyTo       | The email address to which replies should be sent (can differ from `from`). |
| date          | The date and time when the email was sent, usually in RFC 2822 format. (UTC)      |
| id            | The unique Gmail-assigned ID of the message.                                |
| labelIds      | Array of Gmail label IDs applied to the message (e.g., `SENT`, `IMPORTANT`).|
| messageId     | The unique identifier of the message used in email headers for threading.   |
| threadId      | The ID of the conversation (thread) that the message is part of.            |
| headers       | An array of all email headers including metadata like `Subject`, `From`, `Date`, etc. |
| sizeEstimate  | Estimated size of the email in bytes.                                       |
| subject       | The subject line of the email.                                              |
| html          | The HTML version of the email body, if present.                             |
| text          | The plain-text version of the email body.                                   |
| textAsHtml    | The plain-text content converted to basic HTML formatting for display.      |
