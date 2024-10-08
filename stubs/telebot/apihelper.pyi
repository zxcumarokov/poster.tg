from _typeshed import Incomplete
from telebot import types as types, util as util

format_header_param: Incomplete
logger: Incomplete
proxy: Incomplete
session: Incomplete
API_URL: Incomplete
FILE_URL: Incomplete
CONNECT_TIMEOUT: int
READ_TIMEOUT: int
LONG_POLLING_TIMEOUT: int
SESSION_TIME_TO_LIVE: int
RETRY_ON_ERROR: bool
RETRY_TIMEOUT: int
MAX_RETRIES: int
RETRY_ENGINE: int
CUSTOM_SERIALIZER: Incomplete
CUSTOM_REQUEST_SENDER: Incomplete
ENABLE_MIDDLEWARE: bool

def get_me(token): ...
def log_out(token): ...
def close(token): ...
def get_file(token, file_id): ...
def get_file_url(token, file_id): ...
def download_file(token, file_path): ...
def send_message(token, chat_id, text, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, link_preview_options: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def set_webhook(token, url: Incomplete | None = None, certificate: Incomplete | None = None, max_connections: Incomplete | None = None, allowed_updates: Incomplete | None = None, ip_address: Incomplete | None = None, drop_pending_updates: Incomplete | None = None, timeout: Incomplete | None = None, secret_token: Incomplete | None = None): ...
def delete_webhook(token, drop_pending_updates: Incomplete | None = None, timeout: Incomplete | None = None): ...
def get_webhook_info(token, timeout: Incomplete | None = None): ...
def get_updates(token, offset: Incomplete | None = None, limit: Incomplete | None = None, timeout: Incomplete | None = None, allowed_updates: Incomplete | None = None, long_polling_timeout: Incomplete | None = None): ...
def get_user_profile_photos(token, user_id, offset: Incomplete | None = None, limit: Incomplete | None = None): ...
def set_message_reaction(token, chat_id, message_id, reaction: Incomplete | None = None, is_big: Incomplete | None = None): ...
def get_chat(token, chat_id): ...
def leave_chat(token, chat_id): ...
def get_chat_administrators(token, chat_id): ...
def get_chat_member_count(token, chat_id): ...
def set_sticker_set_thumbnail(token, name, user_id, thumbnail, format): ...
def replace_sticker_in_set(token, user_id, name, old_sticker, sticker): ...
def set_chat_sticker_set(token, chat_id, sticker_set_name): ...
def delete_chat_sticker_set(token, chat_id): ...
def get_chat_member(token, chat_id, user_id): ...
def forward_message(token, chat_id, from_chat_id, message_id, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None): ...
def copy_message(token, chat_id, from_chat_id, message_id, caption: Incomplete | None = None, parse_mode: Incomplete | None = None, caption_entities: Incomplete | None = None, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def send_dice(token, chat_id, emoji: Incomplete | None = None, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_photo(token, chat_id, photo, caption: Incomplete | None = None, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, caption_entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, has_spoiler: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def send_media_group(token, chat_id, media, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_location(token, chat_id, latitude, longitude, live_period: Incomplete | None = None, reply_markup: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, horizontal_accuracy: Incomplete | None = None, heading: Incomplete | None = None, proximity_alert_radius: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def edit_message_live_location(token, latitude, longitude, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, horizontal_accuracy: Incomplete | None = None, heading: Incomplete | None = None, proximity_alert_radius: Incomplete | None = None, live_period: Incomplete | None = None): ...
def stop_message_live_location(token, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None): ...
def send_venue(token, chat_id, latitude, longitude, title, address, foursquare_id: Incomplete | None = None, foursquare_type: Incomplete | None = None, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, google_place_id: Incomplete | None = None, google_place_type: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_contact(token, chat_id, phone_number, first_name, last_name: Incomplete | None = None, vcard: Incomplete | None = None, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_chat_action(token, chat_id, action, timeout: Incomplete | None = None, message_thread_id: Incomplete | None = None, business_connection_id: Incomplete | None = None): ...
def send_video(token, chat_id, data, duration: Incomplete | None = None, caption: Incomplete | None = None, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, supports_streaming: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, thumbnail: Incomplete | None = None, width: Incomplete | None = None, height: Incomplete | None = None, caption_entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, has_spoiler: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def send_animation(token, chat_id, data, duration: Incomplete | None = None, caption: Incomplete | None = None, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, thumbnail: Incomplete | None = None, caption_entities: Incomplete | None = None, protect_content: Incomplete | None = None, width: Incomplete | None = None, height: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, has_spoiler: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def send_voice(token, chat_id, voice, caption: Incomplete | None = None, duration: Incomplete | None = None, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, caption_entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_video_note(token, chat_id, data, duration: Incomplete | None = None, length: Incomplete | None = None, reply_markup: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, thumbnail: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_audio(token, chat_id, audio, caption: Incomplete | None = None, duration: Incomplete | None = None, performer: Incomplete | None = None, title: Incomplete | None = None, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, thumbnail: Incomplete | None = None, caption_entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def send_data(token, chat_id, data, data_type, reply_markup: Incomplete | None = None, parse_mode: Incomplete | None = None, disable_notification: Incomplete | None = None, timeout: Incomplete | None = None, caption: Incomplete | None = None, thumbnail: Incomplete | None = None, caption_entities: Incomplete | None = None, disable_content_type_detection: Incomplete | None = None, visible_file_name: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, emoji: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def get_method_by_type(data_type): ...
def ban_chat_member(token, chat_id, user_id, until_date: Incomplete | None = None, revoke_messages: Incomplete | None = None): ...
def unban_chat_member(token, chat_id, user_id, only_if_banned): ...
def restrict_chat_member(token, chat_id, user_id, permissions, until_date: Incomplete | None = None, use_independent_chat_permissions: Incomplete | None = None): ...
def promote_chat_member(token, chat_id, user_id, can_change_info: Incomplete | None = None, can_post_messages: Incomplete | None = None, can_edit_messages: Incomplete | None = None, can_delete_messages: Incomplete | None = None, can_invite_users: Incomplete | None = None, can_restrict_members: Incomplete | None = None, can_pin_messages: Incomplete | None = None, can_promote_members: Incomplete | None = None, is_anonymous: Incomplete | None = None, can_manage_chat: Incomplete | None = None, can_manage_video_chats: Incomplete | None = None, can_manage_topics: Incomplete | None = None, can_post_stories: Incomplete | None = None, can_edit_stories: Incomplete | None = None, can_delete_stories: Incomplete | None = None): ...
def set_chat_administrator_custom_title(token, chat_id, user_id, custom_title): ...
def ban_chat_sender_chat(token, chat_id, sender_chat_id): ...
def unban_chat_sender_chat(token, chat_id, sender_chat_id): ...
def set_chat_permissions(token, chat_id, permissions, use_independent_chat_permissions: Incomplete | None = None): ...
def create_chat_invite_link(token, chat_id, name, expire_date, member_limit, creates_join_request): ...
def edit_chat_invite_link(token, chat_id, invite_link, name, expire_date, member_limit, creates_join_request): ...
def revoke_chat_invite_link(token, chat_id, invite_link): ...
def export_chat_invite_link(token, chat_id): ...
def approve_chat_join_request(token, chat_id, user_id): ...
def decline_chat_join_request(token, chat_id, user_id): ...
def set_chat_photo(token, chat_id, photo): ...
def delete_chat_photo(token, chat_id): ...
def set_chat_title(token, chat_id, title): ...
def set_my_description(token, description: Incomplete | None = None, language_code: Incomplete | None = None): ...
def get_my_description(token, language_code: Incomplete | None = None): ...
def set_my_short_description(token, short_description: Incomplete | None = None, language_code: Incomplete | None = None): ...
def get_my_short_description(token, language_code: Incomplete | None = None): ...
def get_my_commands(token, scope: Incomplete | None = None, language_code: Incomplete | None = None): ...
def set_my_name(token, name: Incomplete | None = None, language_code: Incomplete | None = None): ...
def get_my_name(token, language_code: Incomplete | None = None): ...
def set_chat_menu_button(token, chat_id: Incomplete | None = None, menu_button: Incomplete | None = None): ...
def get_chat_menu_button(token, chat_id: Incomplete | None = None): ...
def set_my_default_administrator_rights(token, rights: Incomplete | None = None, for_channels: Incomplete | None = None): ...
def get_my_default_administrator_rights(token, for_channels: Incomplete | None = None): ...
def set_my_commands(token, commands, scope: Incomplete | None = None, language_code: Incomplete | None = None): ...
def get_business_connection(token, business_connection_id): ...
def delete_my_commands(token, scope: Incomplete | None = None, language_code: Incomplete | None = None): ...
def set_chat_description(token, chat_id, description): ...
def pin_chat_message(token, chat_id, message_id, disable_notification: Incomplete | None = None): ...
def unpin_chat_message(token, chat_id, message_id): ...
def unpin_all_chat_messages(token, chat_id): ...
def edit_message_text(token, text, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, parse_mode: Incomplete | None = None, entities: Incomplete | None = None, reply_markup: Incomplete | None = None, link_preview_options: Incomplete | None = None): ...
def edit_message_caption(token, caption, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, parse_mode: Incomplete | None = None, caption_entities: Incomplete | None = None, reply_markup: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def edit_message_media(token, media, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, reply_markup: Incomplete | None = None): ...
def edit_message_reply_markup(token, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None, reply_markup: Incomplete | None = None): ...
def delete_message(token, chat_id, message_id, timeout: Incomplete | None = None): ...
def send_game(token, chat_id, game_short_name, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def set_game_score(token, user_id, score, force: Incomplete | None = None, disable_edit_message: Incomplete | None = None, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None): ...
def get_game_high_scores(token, user_id, chat_id: Incomplete | None = None, message_id: Incomplete | None = None, inline_message_id: Incomplete | None = None): ...
def send_invoice(token, chat_id, title, description, invoice_payload, provider_token, currency, prices, start_parameter: Incomplete | None = None, photo_url: Incomplete | None = None, photo_size: Incomplete | None = None, photo_width: Incomplete | None = None, photo_height: Incomplete | None = None, need_name: Incomplete | None = None, need_phone_number: Incomplete | None = None, need_email: Incomplete | None = None, need_shipping_address: Incomplete | None = None, send_phone_number_to_provider: Incomplete | None = None, send_email_to_provider: Incomplete | None = None, is_flexible: Incomplete | None = None, disable_notification: Incomplete | None = None, reply_markup: Incomplete | None = None, provider_data: Incomplete | None = None, timeout: Incomplete | None = None, max_tip_amount: Incomplete | None = None, suggested_tip_amounts: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def answer_shipping_query(token, shipping_query_id, ok, shipping_options: Incomplete | None = None, error_message: Incomplete | None = None): ...
def answer_pre_checkout_query(token, pre_checkout_query_id, ok, error_message: Incomplete | None = None): ...
def refund_star_payment(token, user_id, telegram_payment_charge_id): ...
def unpin_all_general_forum_topic_messages(token, chat_id): ...
def answer_callback_query(token, callback_query_id, text: Incomplete | None = None, show_alert: Incomplete | None = None, url: Incomplete | None = None, cache_time: Incomplete | None = None): ...
def get_user_chat_boosts(token, chat_id, user_id): ...
def answer_inline_query(token, inline_query_id, results, cache_time: Incomplete | None = None, is_personal: Incomplete | None = None, next_offset: Incomplete | None = None, button: Incomplete | None = None): ...
def get_sticker_set(token, name): ...
def get_custom_emoji_stickers(token, custom_emoji_ids): ...
def set_sticker_keywords(token, sticker, keywords: Incomplete | None = None): ...
def set_sticker_mask_position(token, sticker, mask_position: Incomplete | None = None): ...
def upload_sticker_file(token, user_id, sticker, sticker_format): ...
def set_custom_emoji_sticker_set_thumbnail(token, name, custom_emoji_id: Incomplete | None = None): ...
def set_sticker_set_title(token, name, title): ...
def delete_sticker_set(token, name): ...
def set_sticker_emoji_list(token, sticker, emoji_list): ...
def create_new_sticker_set(token, user_id, name, title, stickers, sticker_type: Incomplete | None = None, needs_repainting: Incomplete | None = None): ...
def add_sticker_to_set(token, user_id, name, sticker): ...
def set_sticker_position_in_set(token, sticker, position): ...
def delete_sticker_from_set(token, sticker): ...
def answer_web_app_query(token, web_app_query_id, result: types.InlineQueryResultBase): ...
def create_invoice_link(token, title, description, payload, provider_token, currency, prices, max_tip_amount: Incomplete | None = None, suggested_tip_amounts: Incomplete | None = None, provider_data: Incomplete | None = None, photo_url: Incomplete | None = None, photo_size: Incomplete | None = None, photo_width: Incomplete | None = None, photo_height: Incomplete | None = None, need_name: Incomplete | None = None, need_phone_number: Incomplete | None = None, need_email: Incomplete | None = None, need_shipping_address: Incomplete | None = None, send_phone_number_to_provider: Incomplete | None = None, send_email_to_provider: Incomplete | None = None, is_flexible: Incomplete | None = None): ...
def send_poll(token, chat_id, question, options, is_anonymous: Incomplete | None = None, type: Incomplete | None = None, allows_multiple_answers: Incomplete | None = None, correct_option_id: Incomplete | None = None, explanation: Incomplete | None = None, explanation_parse_mode: Incomplete | None = None, open_period: Incomplete | None = None, close_date: Incomplete | None = None, is_closed: Incomplete | None = None, disable_notification: bool = False, reply_markup: Incomplete | None = None, timeout: Incomplete | None = None, explanation_entities: Incomplete | None = None, protect_content: Incomplete | None = None, message_thread_id: Incomplete | None = None, reply_parameters: Incomplete | None = None, business_connection_id: Incomplete | None = None, question_parse_mode: Incomplete | None = None, question_entities: Incomplete | None = None, message_effect_id: Incomplete | None = None): ...
def create_forum_topic(token, chat_id, name, icon_color: Incomplete | None = None, icon_custom_emoji_id: Incomplete | None = None): ...
def edit_forum_topic(token, chat_id, message_thread_id, name: Incomplete | None = None, icon_custom_emoji_id: Incomplete | None = None): ...
def close_forum_topic(token, chat_id, message_thread_id): ...
def reopen_forum_topic(token, chat_id, message_thread_id): ...
def delete_forum_topic(token, chat_id, message_thread_id): ...
def unpin_all_forum_topic_messages(token, chat_id, message_thread_id): ...
def get_forum_topic_icon_stickers(token): ...
def stop_poll(token, chat_id, message_id, reply_markup: Incomplete | None = None): ...
def edit_general_forum_topic(token, chat_id, name): ...
def close_general_forum_topic(token, chat_id): ...
def reopen_general_forum_topic(token, chat_id): ...
def hide_general_forum_topic(token, chat_id): ...
def unhide_general_forum_topic(token, chat_id): ...
def delete_messages(token, chat_id, message_ids): ...
def forward_messages(token, chat_id, from_chat_id, message_ids, disable_notification: Incomplete | None = None, message_thread_id: Incomplete | None = None, protect_content: Incomplete | None = None): ...
def copy_messages(token, chat_id, from_chat_id, message_ids, disable_notification: Incomplete | None = None, message_thread_id: Incomplete | None = None, protect_content: Incomplete | None = None, remove_caption: Incomplete | None = None, show_caption_above_media: Incomplete | None = None): ...
def convert_input_media(media): ...
def convert_input_media_array(array): ...

class ApiException(Exception):
    function_name: Incomplete
    result: Incomplete
    def __init__(self, msg, function_name, result) -> None: ...

class ApiHTTPException(ApiException):
    def __init__(self, function_name, result) -> None: ...

class ApiInvalidJSONException(ApiException):
    def __init__(self, function_name, result) -> None: ...

class ApiTelegramException(ApiException):
    result_json: Incomplete
    error_code: Incomplete
    description: Incomplete
    def __init__(self, function_name, result, result_json) -> None: ...
