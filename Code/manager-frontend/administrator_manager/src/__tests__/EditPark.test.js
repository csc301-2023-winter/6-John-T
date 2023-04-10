import React from 'react';
import EditPark from '../EditPark/EditPark';
import Adapter from 'enzyme-adapter-react-16';
import Enzyme, { shallow } from 'enzyme';
import toJSON from "enzyme-to-json"
import { BrowserRouter } from 'react-router-dom';

Enzyme.configure({adapter: new Adapter()});

it('renders correctly', () => {
    const tree = shallow(<BrowserRouter> <EditPark/> </BrowserRouter>)
expect(toJSON(tree)).toMatchSnapshot(); 
});