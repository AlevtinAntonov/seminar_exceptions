# 2. Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете
# получить? код приложен в виде картинки к семинару

# public static int sum2d(String[][] arr) {
#   int sum = 0;
#   for (int i = 0; i < arr.length; i++) {
#     for (int j = 0; j < 5; j++) {
#       int val = Integer.parseInt(arr[i][j]);
#       sum += val;
#     }
#   }
# return sum;
# }
RuntimeException
NullPointerException
ArrayIndexOutOfBoundsException
NumberFormatException
