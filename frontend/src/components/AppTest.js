import React, {Component} from 'react';


class AppTest extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        this.test = "test";
        fetch("api/main")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return {placeholder: "Something went wrong!"};
                    });
                }
                return response.json();
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <ul>
                {this.state.data.map(contact => {
                    return (
                        <li key={contact.id}>
                            <b>{contact.name}</b> - {contact.email}
                        </li>
                    );
                })}
            </ul>
        );
    }
}

export default AppTest;