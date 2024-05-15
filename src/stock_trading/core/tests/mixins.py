# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import status


class APITestCaseMixin:
    def assertUnauthorizedView(
            self,
            url,
            data={},
            message="Unauthorized access, should not be allowed to perform `view` request."
    ):
        """
        Do not allow `view` request for unauthorized access.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, message)

    def assertUnauthorizedAdd(
            self,
            url,
            data={},
            message="Unauthorized access, should not be allowed to perform `add` request."
    ):
        """
        Do not allow `add` request for unauthorized access.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, message)

    def assertUnauthorizedChange(
            self,
            url,
            data={},
            message="Unauthorized access, should not be allowed to perform `change` request."
    ):
        """
        Do not allow `change` request for unauthorized access.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, message)

    def assertUnauthorizedDelete(
            self,
            url,
            data={},
            message="Unauthorized access, should not be allowed to perform `delete` request."
    ):
        """
        Do not allow `delete` request for unauthorized access.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, message)

    def assertForbidView(
            self,
            url,
            data={},
            message="Unauthenticated user should not be allowed to perform `view` request."
    ):
        """
        Do not allow `view` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, message)

    def assertForbidAdd(
            self,
            url,
            data={},
            message="Unauthenticated user should not be allowed to perform `add` request."
    ):
        """
        Do not allow `add` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, message)

    def assertForbidChange(
            self,
            url,
            data={},
            message="Unauthenticated user should not be allowed to perform `change` request."
    ):
        """
        Do not allow `change` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, message)

    def assertForbidDelete(
            self,
            url,
            data={},
            message="Unauthenticated user should not be allowed to perform `delete` request."
    ):
        """
        Do not allow `delete` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, message)

    def assertCanView(
            self,
            url,
            data={},
            message="Unauthenticated user should be allow to perform `view` request."
    ):
        """
        Allow `view` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, message)

    def assertCanAdd(
            self,
            url,
            data={},
            message="Unauthenticated user should be allow to perform `add` request."
    ):
        """
        Allow `add` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, message)
        return response

    def assertCanChange(
            self,
            url,
            data={},
            message="Unauthenticated user should be allow to perform `change` request."
    ):
        """
        Allow `change` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, message)
        return response

    def assertCanDelete(
            self,
            url,
            data={},
            message="Unauthenticated user should be allow to perform `delete` request."
    ):
        """
        Allow `delete` request for unauthenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, message)

    def assertUserForbidView(
            self,
            url,
            data={},
            message="User should not be allowed to perform `view` request."
    ):
        """
        Do not allow `view` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        self.assertForbidView(url, data, message)

    def assertUserForbidAdd(
            self,
            url,
            data={},
            message="User should not be allowed to perform `add` request."
    ):
        """
        Do not allow `add` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        self.assertForbidAdd(url, data, message)

    def assertUserForbidChange(
            self,
            url,
            data={},
            message="User should not be allowed to perform `change` request."
    ):
        """
        Do not allow `change` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        self.assertForbidChange(url, data, message)

    def assertUserForbidDelete(
            self,
            url,
            data={},
            message="User should not be allowed to perform `delete` request."
    ):
        """
        Do not allow `delete` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertForbidDelete(url, data, message)

    def assertUserCanView(
            self,
            url,
            data={},
            message="User should be allow to perform `view` request."
    ):
        """
        Allow `view` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        self.assertCanView(url, data, message)

    def assertUserCanAdd(
            self,
            url,
            data={},
            message="User should be allow to perform `add` request."
    ):
        """
        Allow `add` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        return self.assertCanAdd(url, data, message)

    def assertUserCanChange(
            self,
            url,
            data={},
            message="User should be allow to perform `change` request."
    ):
        """
        Allow `change` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        return self.assertCanChange(url, data, message)

    def assertUserCanDelete(
            self,
            url,
            data={},
            message="User should be allow to perform `delete` request."
    ):
        """
        Allow `delete` request for authenticated user.

        :param url:
        :param data:
        :param message:
        :return:
        """
        self.assertIn('_auth_user_id', self.client.session, "User is not logged in.")
        self.assertCanDelete(url, data, message)

    def assertFailedAdd(
            self,
            url,
            data={},
            message="Bad request, `add` action performed should failed."
    ):
        """
        Failed `add` request.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, message)

    def assertFailedChange(
            self,
            url,
            data={},
            message="Bad request, `change` action performed should failed."
    ):
        """
        Failed `change` request.

        :param url:
        :param data:
        :param message:
        :return:
        """
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, message)
