import React from 'react';
import NewPark from '../NewPark/NewPark';
import Adapter from 'enzyme-adapter-react-16';
import Enzyme, { shallow } from 'enzyme';
import toJSON from "enzyme-to-json"
import { BrowserRouter } from 'react-router-dom';


Enzyme.configure({adapter: new Adapter()});

it('renders correctly', () => {
    const tree = shallow(<BrowserRouter> <NewPark/> </BrowserRouter>)
expect(toJSON(tree)).toMatchSnapshot(); 
});