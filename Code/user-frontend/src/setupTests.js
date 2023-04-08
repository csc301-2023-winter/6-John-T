// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
// import '@testing-library/jest-dom';
// import { configure } from 'enzyme';
const configure = require('enzyme').configure;
// import Adapter from 'enzyme-adapter-react-16';
const Adapter = require('enzyme-adapter-react-16');
// import 'jest-enzyme';
require('jest-enzyme');
configure({ adapter: new Adapter() });