class test {
    public static void main(String args[]) {
        // String a = "1abc234ka1784j910001dj8h1ohd1128hf9";
        // char x[] = a.toCharArray();
        // for (int i = 0; i < x.length - 3; i++) {
        // if (Character.isDigit(x[i])) {
        // int j = i + 1;

        // for (; j < x.length && Character.isDigit(x[j]); j++) {
        // }

        // if (j - i > 3) {
        // System.out.println(a.substring(i, j));
        // }

        // i = j - 1;
        // }
        // }

        String b = "babaddab";
        int size = b.length();
        for (int i = 0; i < b.length(); i++) {
            for (int j = 0; j + size <= b.length(); j++) {
                String check = b.substring(j, j + size);
                String rev = (new StringBuffer(check).reverse()).toString();
                if (check.equals(rev)) {
                    System.out.println(check);
                }
            }
            size--;
        }
    }
}
