React 18: Comprehensive Overview

[My Notes](https://github.com/kurtzace/diary-2024/issues/10)

---

## Introduction

- Diving deeper into React 18
- Covering testing, compliance, server-side rendering, and asynchronous operations

---

## Testing in React

- **Jest for Unit Testing**:
  - Popular testing framework for React applications
  - Example:
    ```jsx
    describe("Math functions", () => {
      test("Multiplies by two", () => {
        expect(timesTwo(4)).toBe(8);
      });
    });
    ```

- **React Testing Library**:
  - Focuses on testing components in a way that resembles user interactions
  - Example:
    ```jsx
    import { render, fireEvent } from "@testing-library/react";
    test("renders a star", () => {
      const { getByText } = render(<Star />);
      expect(getByText(/Great Star/)).toHaveTextContent("Great Star");
    });
    ```

- **Testing Hooks with renderHook**:
  ```jsx
  import { renderHook } from '@testing-library/react-hooks';
  const { result } = renderHook(() => useCustomHook());
  expect(result.current.value).toBe(someValue);
  ```

---

## Compliance and Best Practices

- **Accessibility**:
  - Use tools like eslint-plugin-jsx-a11y to ensure accessibility compliance

- **Linting**:
  - Use ESLint for enforcing code quality
  - Example:
    ```bash
    npm install eslint-plugin-react-hooks --save-dev
    ```

- **Prettier for Code Formatting**:
  - Auto-formats code for consistency
  - Example:
    ```bash
    sudo npm install -g prettier
    prettier --write "src/**/*.js"
    ```

- **Type Checking**:
  - **PropTypes**: Simple runtime type checking
    ```jsx
    import PropTypes from 'prop-types';
    Component.propTypes = {
      name: PropTypes.string
    };
    ```

  - **TypeScript**: Static type checking
    ```typescript
    type Props = {
      item: string;
    };
    ```

---

## Server-Side Rendering (SSR)

- **ReactDOMServer**:
  - Render components to static HTML
  - Example:
    ```jsx
    import ReactDOMServer from 'react-dom/server';
    const app = ReactDOMServer.renderToString(<App />);
    ```

- **Next.js for SSR**:
  - A React framework for server-side rendering and static site generation
  - Example:
    ```jsx
    export async function getServerSideProps() {
      return { props: { data: await fetchData() } };
    }
    ```

---

## Asynchronous Operations

- **Fetching Data with useEffect**:
  - Best practice to handle API calls
  - Example:
    ```jsx
    useEffect(() => {
      fetchData().then(data => setData(data));
    }, []);
    ```

- **GraphQL with Apollo Client**:
  ```jsx
  import { ApolloClient, InMemoryCache, gql } from '@apollo/client';
  const client = new ApolloClient({
    uri: 'https://example.com/graphql',
    cache: new InMemoryCache()
  });

  const { data } = useQuery(gql`
    query GetItems {
      items {
        id
        name
      }
    }
  `);
  ```

- **Async/Await for Simplified Asynchronous Code**:
  ```jsx
  async function fetchData() {
    const response = await fetch('/api/data');
    return response.json();
  }
  ```

---

## Beyond the Web: React Native

- **React Native for Mobile Apps**:
  - Build native apps using React
  - Uses components like `<View>` and `<Text>` instead of `<div>` and `<span>`

- **Expo for Rapid Development**:
  - Toolchain for building cross-platform apps
  - Example:
    ```bash
    expo init MyApp
    ```

---

## Error Handling and Lazy Loading

- **Error Boundaries**:
  ```jsx
  class ErrorBoundary extends React.Component {
    state = { hasError: false };
    static getDerivedStateFromError(error) {
      return { hasError: true };
    }
    render() {
      if (this.state.hasError) return <h1>Something went wrong.</h1>;
      return this.props.children;
    }
  }
  ```

- **Lazy Loading with React.lazy**:
  ```jsx
  const LazyComponent = React.lazy(() => import('./LazyComponent'));
  <Suspense fallback={<div>Loading...</div>}>
    <LazyComponent />
  </Suspense>
  ```

---

## More Slides

- **Prezi Slides**:
  - [React 18 New Features - Unleash the future](https://prezi.com/view/UZbu7UZqCLAMzyYlg9Um/)
  - [React 18 Performance Practices](https://prezi.com/view/DF6bz4yIdXALaYIIIeCe/)
  - [React 18 Testing , Complaince, SSE](https://prezi.com/view/QxDsy9QRSssyJwjxwNWp/)

<iframe src="https://prezi.com/p/embed/UZbu7UZqCLAMzyYlg9Um/" id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay; fullscreen" height="169" width="300"></iframe> 
<iframe src="https://prezi.com/p/embed/DF6bz4yIdXALaYIIIeCe/" id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay; fullscreen" height="169" width="300"></iframe> 
<iframe src="https://prezi.com/p/embed/QxDsy9QRSssyJwjxwNWp/" id="iframe_container" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay; fullscreen" height="169" width="300"></iframe>
