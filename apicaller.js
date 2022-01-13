const OpenAI = require('openai-api');
require('dotenv').config();
// Load your key from an environment variable or secret management service
// (do not include your key directly in your code)
const OPENAITOKEN = process.env.OPENAITOKEN;
const openai = new OpenAI(OPENAITOKEN);
function getFullSentence(prompt) {
    (async () => {
        const gptResponse = await openai.complete({
            engine: 'davinci',
            model: 'ada:ft-thegoats-2022-01-07-03-13-15',
            prompt: prompt,
            maxTokens: 5,
            temperature: 0.9,
            topP: 1,
            presencePenalty: 0,
            frequencyPenalty: 0,
            bestOf: 1,
            n: 1,
            stream: false,
            stop: ['\n', "testing"]
        });

        return gptResponse.data[1];
    })();
}
console.log(getFullSentence("Stephen Curry has recently"));
