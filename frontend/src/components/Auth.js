import React, {Fragment, useEffect, useState} from "react";
import {render} from "react-dom";
import AppTest from "./AppTest";


const Navbar = () => {
    const [isAuth, setIsAuth] = useState(false);
    const [session, setSession] = useState("");

    useEffect(() => {
        fetch("accounts/profile/session")
            .then(res => res.json())
            .then((result) => {
                setSession(result)
                if (result.SessionID !== null)
                    setIsAuth(true)
            });
    }, []);

    return (
        <div>
            <h3>Victoria Rossi Auth</h3>
            <ul>
                {isAuth === true ? (
                    <Fragment>
                        {' '}
                        <h4>ИД сессии: {session.SessionID}</h4>
                    </Fragment>
                ) : (
                    <Fragment>
                        {' '}
                    </Fragment>
                )}
            </ul>
           <AppTest/>
        </div>
    );
};

export default Navbar;

const container = document.getElementById('auth');
render(<Navbar/>, container);