import { useNavigate } from 'react-router-dom';

import HomeCSS from '../../home/styles/main.module.css';

export default function RegisterComponent() {
    const navigate = useNavigate();

    return (
        <>
            <div className={HomeCSS.container}>
                <div className={HomeCSS.content}>
                    <h1 className={HomeCSS.title}>Projeto Integrador</h1>
                </div>
            </div>
        </>
    );
}