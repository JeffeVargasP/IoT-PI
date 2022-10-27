import { HomePage } from "./pages/home/home_page";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

export const App = () => {

    return (
        <Router >
            <Routes>
                <Route path='/home' element={<HomePage />} />
                <Route path='*' element={<h1></h1>} />
            </Routes>
        </Router >
    );
}