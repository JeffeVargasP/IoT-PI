const startBtn = document.querySelector('#start');
const output = document.querySelector('#output');

export default function start() {
    const recognition = new webkitSpeechRecognition();
    recognition.interimResults = true;
    recognition.lang = "pt-BR";
    recognition.continuous = true;
    recognition.start();

    recognition.onresult = (event) => {
        const results = event.results;
        const transcript = results[results.length - 1][0].transcript;
        output.textContent = transcript;
    }
}