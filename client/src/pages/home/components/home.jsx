import { useNavigate } from 'react-router-dom';

import '../../home/styles/main.css';

export default function RegisterComponent() {
    const navigate = useNavigate();

    return (
        <>
            <div className='container'>
                <div className='content'>
                    <div className='title'>
                        <h1 className='title_animation'>Fatec</h1>
                        <h1 className='title_animation'>Projeto Integrador</h1>
                    </div>
                    <button>
                        <div className='border_button'></div>
                    </button>
                </div>
            </div>
        </>
    );
}