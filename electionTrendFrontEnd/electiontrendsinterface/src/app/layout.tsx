"use client";

import { ReactNode } from "react";

const Layout = ({ children }: { children: ReactNode }) => {

  return (
    <html lang='en'>
      <body style={{'marginTop': '100px'}}>
        <main>{children}</main>
      </body>
    </html>
  );
};

export default Layout;

