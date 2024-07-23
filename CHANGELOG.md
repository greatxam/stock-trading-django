# Stock Trading

## [Unreleased]
- Get live stock data

## [0.0.24] - 2024-07-23
### Added
- Cron service

### Changed
- Update Django settings
- Update Dockerfile
- Docker entrypoint for cron service

## [0.0.23] - 2024-07-21
### Added
- Admin transaction filter

## [0.0.22] - 2024-07-21
### Added
- Admin stock search
- Admin transaction search
- Admin portfolio search

## [0.0.21] - 2024-07-21
### Changed
- Portfolio average price computation

## [0.0.20] - 2024-07-21
### Change
- Order computation discrepancy

## [0.0.19] - 2024-07-21
### Added
- Set WSGI application group

## [0.0.18] - 2024-07-20
### Added
- Add field `trades` to `transaction`
- Transaction service `process_transaction`
- Transaction service `match_order_transaction`
- Transaction service `clone_transaction`
- Transaction service `clear_transaction`

### Changed
- Update transaction service `process_order_transaction`
- Update portfolio service `update_portfolio`

## [0.0.17] - 2024-07-20
### Added
- Add field `is_order` to `transaction`

## [0.0.16] - 2024-07-18
### Added
- Transaction `pre_save` signal

### Changed
- Portfolio service `transaction` typo

### Removed
- Order serializer `save`

## [0.0.15] - 2024-07-18
### Changed
- Environment Variable Settings

### Removed
- Remove `local.env` file

## [0.0.14] - 2024-07-18
### Added
- Configuration wiki
- OAuth application wiki

## [0.0.13] - 2024-07-17
### Changed
- Trade serializer related stock field

## [0.0.12] - 2024-07-15
### Added
- Stock related field

## [0.0.11] - 2024-07-10
### Added
- CORS middleware

## [0.0.10] - 2024-05-17
### Added
- Postman collection and environment

## [0.0.9] - 2024-05-17
### Added
- Cron package
- Process order transaction command
- Process bulk transaction command
- Schedule process commands

### Changed
- Use user `pk` as user's folder

## [0.0.8] - 2024-05-17
### Added
- Create `core` model `Portfolio`
- Portfolio admin
- Portfolio services
- Portfolio API views
- Transaction `post_save` signal

## [0.0.8] - 2024-05-16
### Added
- Upload bulk order CSV file and process
- Upload bulk order CSV file and store only

## [0.0.7] - 2024-05-16
### Added
- Trade services
- Trade API views
- Trade API permissions
- Trade API unit tests

## [0.0.6] - 2024-05-16
### Added
- Order services
- Order API views
- Order API permissions
- Order API unit tests
- Return test client `response` from `APITestCaseMixins`

### Changed
- Order manager queryset filter
- Alter field `quantity` on `transaction` in `core`
- Alter field `type` on `transaction` in `core`
- Alter field `user` on `transaction` in `core`

### Removed
- Default `test.py` file

## [0.0.5] - 2024-05-15
### Added
- Unit test for duplicated `code` field on `stock` in `core`
- Unit test for duplicated `name` field on `stock` in `core`

### Changed
- Alter field `code` on `stock` in `core` module
- Alter field `name` on `stock` in `core` module

## [0.0.4] - 2024-05-15
### Added
- Docker ignore
- Static directory
- Media directory

### Changed
- Docker compose volume mount


## [0.0.3] - 2024-05-15
### Added
- Stock API permissions
- Stock API unit testing

## [0.0.2] - 2024-05-15
### Added
- Django Rest Framework
- Django OAuth Toolkit
- Django CORS Headers
- Stock API views

## [0.0.1] - 2024-05-15
### Added
- Stock Trading `Core` module
- Create `core` model `Stock`
- Create `core` model `Transaction`
- Create `core` proxy model `Order`
- Create `core` proxy model `Trade`

## [0.0.0] - 2024-05-15
### Added
- Django Framework
- Dockerfile
