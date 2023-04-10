import React from 'react';
import EditBench from '../EditBench/EditBench';
import Adapter from 'enzyme-adapter-react-16';
import Enzyme, { shallow } from 'enzyme';
import toJSON from "enzyme-to-json"
import { BrowserRouter } from 'react-router-dom';

Enzyme.configure({adapter: new Adapter()});

it('renders correctly', () => {
    const tree = shallow(<BrowserRouter> <EditBench/> </BrowserRouter>)
expect(toJSON(tree)).toMatchSnapshot(); 
});