import Enzyme, {shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Profile from '../Profile/Profile';
import { BrowserRouter as Router} from 'react-router-dom';
import toJson from 'enzyme-to-json';

Enzyme.configure({adapter: new Adapter()});

test('renders learn react link', () => {
  const test = shallow(<Router><Profile/></Router>);
  expect(toJson(test)).toMatchSnapshot();
});
