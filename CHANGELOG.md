# Stock Trading

## [Unreleased]
- Get live stock data
- Placing stock order
- Upload CSV file for bulk trades
- Cron job for CSV bulk trades
- Get total invested value per stock

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
