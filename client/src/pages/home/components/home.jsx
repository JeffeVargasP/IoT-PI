import { useNavigate } from 'react-router-dom';

import '../../home/styles/main.css';
import start from '../../../index.js';

export default function RegisterComponent() {
    const navigate = useNavigate();

    return (
            <div className='container'>
                <div className='content'>
                    <div className='title'>
                        <h1 className='title_animation' id="output"></h1>
                        <h1 className='title_animation' id="assistent">Projeto Integrador</h1>
                    </div>
                    <button id="start" onClick={start}>
                        <div className='border_button'></div>
                    </button>
                </div>
            </div>
    );
}