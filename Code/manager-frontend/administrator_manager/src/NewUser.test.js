import React from 'react';
import ReactDom from 'react-dom';
import renderer from 'react-test-renderer';
import NewUser from '../src/NewUser/NewUser';
it('renders correctly', () => {
   const tree = renderer
    .create(NewUser)
    .toJSON();
  expect(tree).toMatchSnapshot(); 
});