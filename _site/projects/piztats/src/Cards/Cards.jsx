import React, {Component} from 'react';
import Card from './CardUI';

class Cards extends Component {
    state = {
        name: '',
        price: '',
        size: '',
        drink: '',
    }

    render() {
        return (
            <div className="container-fluid d-flex justify-content-center">
                <div className="row">
                    <div className="col">
                        <Card />
                    </div>
                    <div className="col">
                        <Card />
                    </div>
                    <div className="col">
                        <Card />
                    </div>
                </div>
            </div>
        );
    }
}

export default Cards;