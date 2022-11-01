(() => {
    const startBtn = document.querySelector('#start');
    const output = document.querySelector('#output');

    function start() {
        const recognition = new webkitSpeechRecognition();
        recognition.interimResults = true;
        recognition.lang = "pt-BR";
        recognition.continuous = true;
        recognition.start();
        // This event happens when you talk in the microphone
        recognition.onresult = function(event) {
            for (let i = event.resultIndex; i < event.results.length; i++) {
                if (event.results[i].isFinal) {
                    // Here you can get the string of what you told
                    const content = event.results[i][0].transcript.trim();
                    output.textContent = content;
                }
            }
        };
    };
    startBtn.addEventListener('click', () => start());
})();