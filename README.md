# Ecommerce Website

## Hướng dẫn đẩy (push) code lên branch

1. **Khởi tạo repository Git**:
    ```sh
    git init
    ```

2. **Thêm tất cả các thay đổi vào staging area**:
    ```sh
    git add .
    ```

3. **Commit các thay đổi với một thông điệp commit**:
    ```sh
    git commit -m "your update"
    ```

4. **Đẩy (push) code lên branch**:
    ```sh
    git push origin "your branch"
    ```

5. **Tạo personal access token trên GitHub**:
    - Vào `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`
    - Nhấn `Generate new token` để tạo mật khẩu.

### Ví dụ cụ thể

Giả sử bạn muốn đẩy code lên branch `feature-branch`, bạn sẽ thực hiện các lệnh sau:

1. Khởi tạo repository Git:
    ```sh
    git init
    ```

2. Thêm tất cả các thay đổi vào staging area:
    ```sh
    git add .
    ```

3. Commit các thay đổi với một thông điệp commit:
    ```sh
    git commit -m "Added new feature"
    ```

4. Đẩy code lên branch `feature-branch`:
    ```sh
    git push origin feature-branch
    ```

5. Tạo personal access token trên GitHub:
    - Vào `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`
    - Nhấn `Generate new token` để tạo mật khẩu.

Lưu ý: Khi bạn đẩy code lên GitHub lần đầu tiên hoặc khi bạn cần xác thực, bạn sẽ cần sử dụng personal access token thay vì mật khẩu tài khoản GitHub.
