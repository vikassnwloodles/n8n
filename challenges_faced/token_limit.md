Bad request - please check your parameters
This model's maximum context length is 8192 tokens. However, your messages resulted in 101146 tokens. Please reduce the length of the messages.

We are sending 13x more tokens to the model.
Need to reduce this.
Currently on 10th of May, there are 80 emails in inbox from last 3 days and 4 email in sent emails section from last 1 day.
We can filter out and send only unread emails from last 3 days instead of sending all inbox emails from last 3 days.

----------------------------------------------------------------------------------------------

After fetching only send and unread emails from inbox, we are still getting token limit error:

Bad request - please check your parameters
This model's maximum context length is 8192 tokens. However, your messages resulted in 87618 tokens. Please reduce the length of the messages.

though we are now sending 56 unread + 4 sent emails data to the model.
Still it is 11x more tokens than model expected.
----------------------------------------------------------------------------------------------

Bad request - please check your parameters [item 4]
This model's maximum context length is 8192 tokens. However, your messages resulted in 10222 tokens. Please reduce the length of the messages.

Now we have making batches of emails having 6 emails per batch and sending to gpt for summarization.
Then we are sending those summaries again to gpt to generate daily brief.

Trying to reduce the batch size.

----------------------------------------------------------------------------------------------