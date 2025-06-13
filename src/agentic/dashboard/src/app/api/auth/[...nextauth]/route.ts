import NextAuth from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import type { NextAuthOptions } from "next-auth";

export const authOptions: NextAuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async jwt({ token, profile }) {
      if (profile) {
        token.name = profile.name;
        token.email = profile.email;
      }
      return token;
    },
    async session({ session, token }) {
      session.user = session.user || {};
      session.user.name = token.name as string | undefined;
      session.user.email = token.email as string | undefined;
      return session;
    },
  },
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
