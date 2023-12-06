import { OpenAI}from 'gpt-x';
import dotenv from 'dotenv';
dotenv.config();
console.log(process.env.OPENAITOKEN)
// Load your key from an environment variable or secret management service
// (do not include your key directly in your code)
const openai = new OpenAI(process.env.API_KEY, 'thegoats');
async function getFullSentence(prompt) {
    const completion = await openai.completeFromModel('ada:ft-thegoats-2022-01-07-03-13-15', {
        prompt: prompt
    });

    return completion;
}
console.log(getFullSentence("Stephen Curry has recently"));

