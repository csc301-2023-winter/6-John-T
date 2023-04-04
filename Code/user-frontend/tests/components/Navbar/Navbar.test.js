import React from 'react';
import { shallow } from 'enzyme';
import Navbar from '../../../src/components/Navbar/Navbar.js';
test('should test Navbar component', () => {
 const wrapper = shallow(<Navbar />);
 expect(wrapper).toMatchSnapshot();
});